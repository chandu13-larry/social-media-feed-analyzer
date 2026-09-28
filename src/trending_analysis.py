import pandas as pd

# Read cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Calculate engagement
df["engagement"] = (
    df["likes"] +
    df["comments"] +
    df["shares"]
)

# --------------------------------
# TRENDING HASHTAGS
# --------------------------------

trending = (
    df.groupby("hashtag")
    .agg(
        posts=("hashtag", "count"),
        total_engagement=("engagement", "sum"),
        average_engagement=("engagement", "mean")
    )
    .sort_values("total_engagement", ascending=False)
)

print("TRENDING HASHTAGS")
print("-----------------")
print(trending.round(2))

# --------------------------------
# TOP TRENDING HASHTAG
# --------------------------------

top_trending = trending.index[0]

print("\nTop trending hashtag:", top_trending)

# --------------------------------
# TOP HASHTAG BY AVERAGE ENGAGEMENT
# --------------------------------

top_average = trending["average_engagement"].idxmax()

print("Highest average engagement hashtag:", top_average)