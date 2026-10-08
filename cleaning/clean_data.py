import pandas as pd

RAW_FILE = "data/raw/books_raw.csv"
OUTPUT_FILE = "data/processed/books_cleaned.csv"

# Load raw data
df = pd.read_csv(RAW_FILE)
print(f"Raw dataset shape: {df.shape}")

# Remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Exact duplicate rows removed: {before - after}")

# Clean price
df["price"] = (
    df["price"].str.replace("£","",regex=False).astype(float)
)

# Convert rating to numeric
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating"] = df["rating"].map(rating_map)

# Clean availability
df["availability"] = df["availability"].str.strip()

# Create in-stock flag
df["in-stock"] = df["availability"].str.lower().eq("in stock")

# Create price bucket
df["price_bucket"] = pd.cut(
    df["price"],
    bins = [0, 20, 40, 60, float("inf")],
    labels = ["Low", "Medium", "High", "Very High"],
    include_lowest=True
)

# Standardized category
df["category"] = df["category"].str.strip()

# Validate data types
print("\nCLEANED DATA TYPES")
print(df.dtypes)

# Validate missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Summary
print("\nCLEANED DATASET SHAPE")
print(df.shape)
print("\nCLEANED FIRST 5 ROWS")
print(df.head())

# Save cleaned data
df.to_csv(
    OUTPUT_FILE,
    index=True
)
print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")