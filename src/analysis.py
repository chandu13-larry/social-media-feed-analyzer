import pandas as pd

# Read cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Convert timestamp back to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])


# -----------------------------
# BASIC DATA ANALYSIS
# -----------------------------

print("SOCIAL MEDIA DATA ANALYSIS")
print("--------------------------")

# Total posts
print("\nTotal posts:", len(df))

# Total likes
print("Total likes:", df["likes"].sum())

# Total comments
print("Total comments:", df["comments"].sum())

# Total shares
print("Total shares:", df["shares"].sum())


# -----------------------------
# AVERAGE ENGAGEMENT
# -----------------------------

average_likes = df["likes"].mean()
average_comments = df["comments"].mean()
average_shares = df["shares"].mean()

print("\nAverage likes:", round(average_likes, 2))
print("Average comments:", round(average_comments, 2))
print("Average shares:", round(average_shares, 2))


# -----------------------------
# TOP PERFORMING POST
# -----------------------------

df["engagement"] = (
    df["likes"] +
    df["comments"] +
    df["shares"]
)

top_post = df.loc[df["engagement"].idxmax()]

print("\nTop performing post:")
print(top_post)


# -----------------------------
# MOST POPULAR HASHTAGS
# -----------------------------

print("\nTop hashtags:")
print(df["hashtag"].value_counts().head())


# -----------------------------
# POSTS BY LOCATION
# -----------------------------

print("\nPosts by location:")
print(df["location"].value_counts())


# -----------------------------
# MOST ACTIVE USERS
# -----------------------------

print("\nMost active users:")
print(df["username"].value_counts().head())