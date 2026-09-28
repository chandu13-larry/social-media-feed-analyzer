
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_social_media_posts.csv")

# Create engagement column
df["engagement"] = df["likes"] + df["comments"] + df["shares"]

# Positive and negative keywords
positive_words = [
    "amazing", "great", "excellent", "good", "happy",
    "love", "best", "awesome", "success", "beautiful",
    "wonderful", "fantastic"
]

negative_words = [
    "bad", "worst", "hate", "sad", "poor",
    "angry", "problem", "failed", "failure", "terrible",
    "boring", "disappointed"
]


def detect_sentiment(text):
    text = str(text).lower()

    positive_count = sum(word in text for word in positive_words)
    negative_count = sum(word in text for word in negative_words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"


# Apply sentiment analysis
df["sentiment"] = df["text"].apply(detect_sentiment)

# Save the new dataset
df.to_csv("data/social_media_sentiment.csv", index=False)

# Display results
print("Sentiment analysis completed.")
print()

print("Sentiment counts:")
print(df["sentiment"].value_counts())

print()

print("Sentiment percentages:")
print(
    (df["sentiment"].value_counts(normalize=True) * 100).round(2)
)

print()

print("Average engagement by sentiment:")
print(
    df.groupby("sentiment")["engagement"].mean().round(2)
)

