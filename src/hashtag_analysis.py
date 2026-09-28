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
# HASHTAG POST COUNT
# --------------------------------

hashtag_posts = df["hashtag"].value_counts()

print("POSTS BY HASHTAG")
print("----------------")
print(hashtag_posts)


# --------------------------------
# TOTAL ENGAGEMENT BY HASHTAG
# --------------------------------

hashtag_engagement = (
    df.groupby("hashtag")["engagement"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOTAL ENGAGEMENT BY HASHTAG")
print("----------------------------")
print(hashtag_engagement)


# --------------------------------
# AVERAGE ENGAGEMENT BY HASHTAG
# --------------------------------

average_engagement = (
    df.groupby("hashtag")["engagement"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVERAGE ENGAGEMENT BY HASHTAG")
print("------------------------------")
print(average_engagement.round(2))