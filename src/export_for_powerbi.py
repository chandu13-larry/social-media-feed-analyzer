import pandas as pd

# Read cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create useful analysis columns
df["engagement"] = (
    df["likes"] +
    df["comments"] +
    df["shares"]
)

df["hour"] = df["timestamp"].dt.hour

df["date"] = df["timestamp"].dt.date

# Save Power BI dataset
df.to_csv(
    "data/social_media_analysis.csv",
    index=False
)

print("Power BI dataset created successfully!")
print("Total records:", len(df))
print("Columns:", list(df.columns))
print("Saved as: data/social_media_analysis.csv")