# 📚 Book Market Intelligence

A data engineering and analytics project that collects, cleans, stores, and analyzes book data from an online book catalog.

The project demonstrates a complete data pipeline using **Python, Web Scraping, Data Cleaning, PostgreSQL, and SQL analysis** to transform raw book information into structured and useful market insights.

---

## 🎯 Project Overview

Online book catalogs contain large amounts of information such as book titles, prices, ratings, availability, and categories. However, this information is often available only as unstructured web data.

**Book Market Intelligence** converts this raw web data into a structured dataset and stores it in PostgreSQL for efficient querying and analysis.

The project follows the pipeline:

```text
Web Source
    ↓
Web Scraping
    ↓
Raw Dataset
    ↓
Data Cleaning & Validation
    ↓
Data Transformation
    ↓
PostgreSQL
    ↓
SQL Analysis
    ↓
Book Market Insights
```

---

## 💡 Problem Statement

Book information available on websites is not always convenient for analysis because it is distributed across web pages and may contain inconsistencies, duplicate records, missing values, or inconsistent categories.

This project solves the problem by:

* Collecting book information automatically
* Creating a structured dataset
* Cleaning and validating the collected data
* Removing duplicate records
* Handling duplicate book titles
* Standardizing categorical information
* Storing the cleaned data in PostgreSQL
* Using SQL queries to analyze the book market

---

## 📊 Dataset

The project collected information for approximately **1,000 books**.

### Dataset Structure

| Column         | Description              |
| -------------- | ------------------------ |
| `title`        | Name of the book         |
| `price`        | Price of the book        |
| `rating`       | Customer rating          |
| `availability` | Availability information |
| `book_url`     | URL of the book          |
| `category`     | Category of the book     |

The resulting dataset contains **1,000 rows and 6 columns**.

---

## 🧹 Data Cleaning

Before storing the data in PostgreSQL, the dataset was inspected and cleaned.

The cleaning process included:

* Checking for duplicate rows
* Identifying duplicate book titles
* Validating missing values
* Inspecting incorrect or inconsistent values
* Reviewing book categories
* Normalizing data formats
* Validating numerical fields such as price and rating
* Preparing the dataset for database storage

The dataset contained:

* **0 duplicate rows**
* **1 duplicate title**

---

## 🗄️ Database

The cleaned data is stored using **PostgreSQL**.

PostgreSQL was selected because it provides:

* Relational data management
* Strong data integrity
* SQL querying capabilities
* Indexing for improved query performance
* Scalability for larger datasets
* Support for analytical queries

The project was developed and tested with **PostgreSQL 18.1**.

---

## 🔍 SQL Analysis

SQL is used to extract insights from the stored book data.

Examples of analysis include:

* Books by category
* Average book price
* Highest and lowest priced books
* Rating distribution
* Availability analysis
* Category-wise pricing
* Category-wise ratings
* Most expensive books
* Books with specific ratings
* Price and rating comparisons

Example analytical query:

```sql
SELECT category, AVG(price) AS average_price
FROM books
GROUP BY category
ORDER BY average_price DESC;
```

This helps identify categories with higher or lower average book prices.

---

## 🏗️ Project Structure

```text
book-market-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scraper/
│   └── ...
│
├── cleaning/
│   └── ...
│
├── database/
│   └── ...
│
├── analysis/
│   └── ...
│
├── pipeline/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

> The exact files and folders may evolve as the project is extended.

---

## ⚙️ Technologies Used

### Programming & Data

* **Python**
* **Pandas**
* **Web Scraping**
* **SQL**

### Database

* **PostgreSQL 18.1**

### Development Tools

* **Git**
* **GitHub**
* **VS Code**
* **Jupyter Notebook**

---

## 🔄 ETL Pipeline

The project follows an ETL-style workflow:

### 1. Extract

Book information is collected from the web using Python-based web scraping.

### 2. Transform

The collected data is:

* Cleaned
* Validated
* Deduplicated
* Normalized
* Prepared for database storage

### 3. Load

The processed dataset is loaded into PostgreSQL.

### 4. Analyze

SQL queries are used to identify patterns and generate book market insights.

---

## 📈 Key Insights

The project can be used to investigate questions such as:

* Which categories contain the most books?
* Which categories have the highest average prices?
* What is the distribution of book ratings?
* Which books are the most expensive?
* How does price vary between categories?
* How many books are available or unavailable?
* Are highly rated books generally more expensive?

These analyses demonstrate how raw web data can be converted into structured information for decision-making.

---

## 🚀 Future Improvements

Possible future improvements include:

* Expanding the dataset from 1,000 books to a much larger collection
* Automating the complete scraping-to-database pipeline
* Adding database indexes for frequently queried columns
* Creating a dashboard for interactive visualization
* Adding scheduled data collection
* Tracking changes in book prices and availability over time
* Adding more detailed market analysis
* Improving data validation and error handling

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Web scraping
* Data collection
* Data cleaning and preprocessing
* Data validation
* PostgreSQL database design
* SQL querying and analysis
* ETL pipeline concepts
* Git and GitHub
* Turning raw web data into structured analytical datasets

---

## 👩‍💻 Author

**Shreya Soma**

Master's in Computer Science

---

## ⭐ Project Purpose

This project was developed as a practical demonstration of **Python, data processing, PostgreSQL, SQL, and data pipeline concepts**, with a focus on converting real-world web data into structured and meaningful insights.
