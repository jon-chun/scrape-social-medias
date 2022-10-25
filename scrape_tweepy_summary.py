# https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9

from base64 import encode
import tweepy

import config_twitter

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

# bearer_token = os.environ.get("BEARER_TOKEN")
my_bearer_token = config_twitter.BEARER_TOKEN

client = tweepy.Client(bearer_token=my_bearer_token)

# SEARCH TWEETS FOR LAST x DAYS
# =============================
# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    # print('hello')
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
        # print('  world')