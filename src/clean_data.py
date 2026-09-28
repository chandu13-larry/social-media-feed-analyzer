import pandas as pd

# Read the dataset
df = pd.read_csv("data/social_media_posts.csv")

print("Before cleaning:")
print(df.dtypes)

# Convert timestamp from text to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Remove duplicate posts
df = df.drop_duplicates()

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check the cleaned data types
print("\nAfter cleaning:")
print(df.dtypes)

# Save cleaned data
df.to_csv("data/cleaned_social_media_posts.csv", index=False)

print("\nCleaning completed!")
print("Total records:", len(df))
print("Saved as: data/cleaned_social_media_posts.csv")