# https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9

# 0. Setup
from datetime import datetime
import tweepy

import config_twitter

consumer_key = config_twitter.API_KEY #Your API/Consumer key 
consumer_secret = config_twitter.API_KEY_SECRET #Your API/Consumer Secret Key
bearer_token = config_twitter.BEARER_TOKEN # Your API/Bearer Token
access_token = config_twitter.ACCESS_TOKEN    #Your Access token key
access_token_secret = config_twitter.ACCESS_TOKEN_SECRET #Your Access token Secret key

# os.environ['BEARER_TOKEN'] = bearer_token

client = tweepy.Client(bearer_token=config_twitter.BEARER_TOKEN)

# 1. Search Last 7 Days

# Context 7/22
# 65: Interests and Hobbies Vertical
# 66: Interests and Hobbies Category
# 67: Interests and Hobbies

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

# If Regular Access: Last 7 days only
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

# If Academic Access: All upto 10M/mo
# tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

# If Academic Access: All within specific time range
"""
# Replace with time period of your choice
start_time = '2020-01-01T00:00:00Z'
end_time = '2020-08-01T00:00:00Z'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                  start_time=start_time,
                                  end_time=end_time, max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)
"""

"""
# Getting/Expanding User Info for each Tweet

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     user_fields=['profile_image_url'], expansions='author_id', max_results=100)

# Get users list from the includes object
users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(user.profile_image_url)
        
"""



# Getting/Expanding Media Info for each Tweet

# Replace with your own search query
query_ls = [# 'midjourney -is:retweet has:media',
            # 'dalle2 -is:retweet has:media',
            'stablediffusion -is:retweet has:media']

# Set max number of results per query
max_per_query = 10

# Accumulate results 
tweets_ls = []

# Loop over each query and accumulate results in tweets_ls
for i, aquery in enumerate(query_ls):
    print(f'\nProcessing query #{i}: {aquery}')
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                         media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                         max_results=max_per_query)
    tweets_ls.append(tweets)
    
    # Get list of media from the includes object

    # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
    # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media

# Loop over each result and process it
    # for i, aresult in enumerate(tweets_ls):
    print('hello')
    media = {m["media_key"]: m for m in tweets.includes['media']}

    for tweet in tweets.data:
        attachments = tweet.data['attachments']
        media_keys = attachments['media_keys']
        print("=================================")
        print(tweet.text.encode('utf8'))
        """
        if media[media_keys[0]].preview_image_url:
            print("----------------------------------")
            print(media[media_keys[0]].preview_image_url)
        """
        if media[media_keys[0]].media_key:
            print("----------------------------------")
            print(media[media_keys[0]].media_key)    
        
        
    # dt_stamp = datetime.now().strftime("%Y%m%d-%I%M%S%p")
    # reddit_outfile = f'reddit_{search_term}_{dt_stamp}_praw_sentiments.csv'
            
"""

# Getting upto 100 Tweets
for tweet in tweets.data:
    print(tweet.text.encode('utf8'))
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)

# Getting >100 Tweets with Paginator
"""


"""
# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    print(tweet.id)

# Writing Tweets to File
# Name and path of the file where you want the Tweets written to
file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(
            limit=1000):
        filehandle.write('%s\n' % tweet.id)
"""