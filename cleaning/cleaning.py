# print("\nDATASET SHAPE")
# print(df.shape)

# print("\nCOLUMNS")
# print(df.columns.tolist())

# print("\nFIRST 5 ROWS")
# print(df.head())

# print("\nDATA TYPES")
# print(df.dtypes)

# print("\nMISSING VALUES")
# print(df.isnull().sum())

# print("\nUNIQUE RATINGS")
# print(df["rating"].unique())

# print("\nUNIQUE AVAILABILITY")
# print(df["availability"].unique())

# print("\nCATEGORY COUNT")
# print(df["category"].nunique())

# print("\nDUPLICATES")
# print(df.duplicated().sum())
# print("\nDUPLICATE TITLES")
# print(df["title"].duplicated().sum())

# print("\nCATEGORIES")
# print(df["category"].sort_values().unique())

# print("\nPRICE SAMPLE")
# print(df["price"].head(10).tolist())
# print("\nPRICE TYPES")
# print(df["price"].map(type).value_counts())

# print("\nAVAILABILITY")
# print(df["availability"].value_counts())

# duplicate_titles = df[
#     df["title"].duplicated(keep= False)
# ].sort_values("title")

# print("\nDUPLICATE TITLES")
# print(duplicate_titles[
#     ["title", "price", "rating", "availability", "book_url", "category"]
# ].to_string(index= False)
# )