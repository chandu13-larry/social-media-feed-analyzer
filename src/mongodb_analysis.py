from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client["social_media_db"]

# Select collection
collection = db["posts"]

print("MONGODB SOCIAL MEDIA ANALYSIS")
print("------------------------------")

# Total posts
total_posts = collection.count_documents({})

print("\nTotal posts:", total_posts)


# --------------------------------
# TOP 5 POSTS BY LIKES
# --------------------------------

top_posts = collection.find().sort("likes", -1).limit(5)

print("\nTOP 5 POSTS BY LIKES")
print("--------------------")

for post in top_posts:
    print(
        "Post ID:", post["post_id"],
        "| Likes:", post["likes"],
        "| Hashtag:", post["hashtag"]
    )


# --------------------------------
# POSTS BY LOCATION
# --------------------------------

print("\nPOSTS BY LOCATION")
print("-----------------")

location_result = collection.aggregate([
    {
        "$group": {
            "_id": "$location",
            "total_posts": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "total_posts": -1
        }
    }
])

for result in location_result:
    print(
        result["_id"],
        ":", result["total_posts"]
    )

    # --------------------------------
# ENGAGEMENT BY HASHTAG
# --------------------------------

print("\nENGAGEMENT BY HASHTAG")
print("---------------------")

hashtag_result = collection.aggregate([
    {
        "$project": {
            "hashtag": 1,
            "engagement": {
                "$add": [
                    "$likes",
                    "$comments",
                    "$shares"
                ]
            }
        }
    },
    {
        "$group": {
            "_id": "$hashtag",
            "total_engagement": {
                "$sum": "$engagement"
            }
        }
    },
    {
        "$sort": {
            "total_engagement": -1
        }
    }
])

for result in hashtag_result:
    print(
        result["_id"],
        ":",
        result["total_engagement"]
    )


# Close connection
client.close()