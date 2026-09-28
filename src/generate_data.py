
import pandas as pd
import random
from datetime import datetime, timedelta

# Number of posts
num_posts = 10000

# Sample data
hashtags = [
    "#Technology",
    "#Bengaluru",
    "#Cricket",
    "#AI",
    "#Python",
    "#DataAnalytics",
    "#Fitness",
    "#Trending"
]

locations = [
    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

positive_texts = [
    "Amazing experience today",
    "Great technology update",
    "Excellent cricket match",
    "I love this new AI tool",
    "Python is really useful",
    "Amazing fitness progress",
    "Beautiful day in Bengaluru",
    "Great work by the team"
]

negative_texts = [
    "Bad experience today",
    "Terrible service",
    "I hate this problem",
    "Very disappointing result",
    "Poor performance today",
    "This failed again",
    "Worst experience ever",
    "I am angry about this"
]

neutral_texts = [
    "Technology update today",
    "Cricket match scheduled today",
    "Python project discussion",
    "Data analytics session today",
    "AI news update",
    "Fitness workout completed",
    "Weather update from Bengaluru",
    "New information available"
]

# Start date
start_date = datetime(2026, 9, 1)

data = []

for i in range(1, num_posts + 1):

    # Random date and time across 30 days
    random_minutes = random.randint(0, 30 * 24 * 60 - 1)
    timestamp = start_date + timedelta(minutes=random_minutes)

    # Random sentiment
    sentiment_type = random.choices(
        ["Positive", "Negative", "Neutral"],
        weights=[50, 20, 30]
    )[0]

    if sentiment_type == "Positive":
        text = random.choice(positive_texts)
    elif sentiment_type == "Negative":
        text = random.choice(negative_texts)
    else:
        text = random.choice(neutral_texts)

    # Random hashtag and location
    hashtag = random.choice(hashtags)
    location = random.choice(locations)

    # Engagement values
    likes = random.randint(10, 1000)
    comments = random.randint(1, 200)
    shares = random.randint(1, 100)

    data.append([
        i,
        timestamp,
        f"user_{random.randint(1, 500)}",
        text,
        hashtag,
        likes,
        comments,
        shares,
        location,
        sentiment_type
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "post_id",
        "timestamp",
        "username",
        "text",
        "hashtag",
        "likes",
        "comments",
        "shares",
        "location",
        "sentiment"
    ]
)

# Sort by timestamp
df = df.sort_values("timestamp").reset_index(drop=True)

# Save dataset
df.to_csv("data/social_media_posts.csv", index=False)

print("New dataset created successfully.")
print("Total posts:", len(df))
print("Date range:", df["timestamp"].min(), "to", df["timestamp"].max())
print()
print("Sentiment distribution:")
print(df["sentiment"].value_counts())

