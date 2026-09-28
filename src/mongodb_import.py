import pandas as pd
from pymongo import MongoClient

# Load cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["social_media_db"]
collection = db["posts"]

# Remove old data
collection.delete_many({})

# Convert DataFrame to records
data = df.to_dict("records")

# Insert new data
collection.insert_many(data)

print("Data successfully inserted into MongoDB!")
print("Total documents:", collection.count_documents({}))