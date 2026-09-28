import pandas as pd

# Read cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create engagement
df["engagement"] = (
    df["likes"] +
    df["comments"] +
    df["shares"]
)

# Extract hour
df["hour"] = df["timestamp"].dt.hour


# -----------------------------
# POSTS PER HOUR
# -----------------------------

posts_per_hour = (
    df.groupby("hour")
    .size()
    .sort_values(ascending=False)
)

print("POSTS PER HOUR")
print("--------------")
print(posts_per_hour)


# -----------------------------
# ENGAGEMENT PER HOUR
# -----------------------------

engagement_per_hour = (
    df.groupby("hour")["engagement"]
    .sum()
    .sort_values(ascending=False)
)

print("\nENGAGEMENT PER HOUR")
print("-------------------")
print(engagement_per_hour)


# -----------------------------
# AVERAGE ENGAGEMENT PER HOUR
# -----------------------------

average_engagement_per_hour = (
    df.groupby("hour")["engagement"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVERAGE ENGAGEMENT PER HOUR")
print("---------------------------")
print(average_engagement_per_hour.round(2))