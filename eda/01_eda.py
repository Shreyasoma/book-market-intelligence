import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/books_cleaned.csv")
print("Shape:", df.shape)
print("Columns:\n", df.columns.tolist())
print("Data types:\n", df.dtypes)

print("Average price:", df["price"].mean())
print("Median price:", df["price"].median())
print("Minimum price:", df["price"].min())
print("Maximum price:", df["price"].max())
print("Standard Deviation:", df["price"].std())

plt.figure(figsize=(10,6))
plt.hist(df["price"], bins=20)
plt.title("distribution of book prices")
plt.xlabel("Price")
plt.ylabel("number of books")
plt.show()