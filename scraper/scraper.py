import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

URL = "https://books.toscrape.com/"

def get_page(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return None
    return BeautifulSoup(response.text, "html.parser")

def scrape_book(book):
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text.strip()
    rating_element = book.select_one("p.star-rating")
    rating = rating_element.get("class")[1]
    availability = book.select_one("p.availability").get_text(strip=True)
    book_url = book.select_one("h3 a")["href"]
    return {
        "title": title,
        "price": price,
        "rating":rating,
        "availability": availability,
        "book_url":book_url
    }

def get_categories():
    soup = get_page(URL)
    if soup is None:
        return []
    categories = []
    category_links = soup.select("div.side_categories ul li ul li a")
    for link in category_links:
        category_name = link.get_text(strip=True)
        category_url = urljoin(URL, link["href"])
        categories.append({
            "name" : category_name,
            "url" : category_url
        })
    return categories

def scrape_page(url, category):
    soup = get_page(url)
    if soup is None:
        return [], None
    books = soup.select("article.product_pod")
    result = []
    for book in books:
        book_data = scrape_book(book)
        book_data["category"] = category
        result.append(book_data)

    next_button = soup.select_one("li.next a")
    if next_button:
        next_url = urljoin(url, next_button["href"])
    else:
        next_url = None
    return result, next_url

def save_to_csv(books, filename):
    if not books:
        print("No books to save")
        return
    fieldnames = books[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(books)
    print(f"Saved {len(books)} books to {filename}")

categories = get_categories()
all_books = []

for category in categories:
    category_name = category["name"]
    category_url = category["url"]
    print(f"\nScraping category: {category_name}")
    curr_url = category_url
    while curr_url:
        print(f"Scraping: {curr_url}")
        books, next_url = scrape_page(curr_url, category_name)
        all_books.extend(books)
        curr_url = next_url
print(f"\nTotal books scraped: {len(all_books)}")
save_to_csv(
    all_books,
    "data/raw/books_raw.csv"
)