import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# Database configuration
DB_USER = "postgres"
DB_PASSWORD = "Shreya@1410"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "book_market"

DATABSE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{quote_plus(DB_PASSWORD)}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABSE_URL)
df = pd.read_csv("data/processed/books_cleaned.csv")
df = df.rename(columns={"in-stock": "in_stock"})
print(f"Loaded {len(df)} books from CSV")

# Get unique categories
categories = df["category"].drop_duplicates().tolist()
print(f"Found {len(categories)} unique categories")

# Insert categories
with engine.begin() as connection:
    for category in categories:
        connection.exec_driver_sql(
            """
            INSERT INTO categories (category_name) 
            VALUES (%s)
            ON CONFLICT (category_name) DO NOTHING
            """,
            (category,)
        )
print("Categories inserted succesfully!")

# Read category ids
category_df = pd.read_sql("SELECT category_id, category_name FROM categories", engine)
print("Category table:")
print(category_df.head())

# Create category mapping
category_mapping = dict(
    zip(
        category_df["category_name"],
        category_df["category_id"]
    )
)
print("Category mapping:")
print(list(category_mapping.items())[:5])

df["category_id"] = df["category"].map(category_mapping)
print("Missing category IDs:")
print(df["category_id"].isnull().sum())

# Select book columns
books_df = df[
    [
        "title",
        "price",
        "rating",
        "availability",
        "book_url",
        "category_id",
        "in_stock",
        "price_bucket"
    ]
].copy()

# Load books in PostgreSQL
books_df.to_sql(
    "books",
    engine,
    if_exists = "append",
    index = False
)
print(f"Succesfully loaded {len(books_df)} books!")