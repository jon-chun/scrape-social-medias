# https://www.freecodecamp.org/news/python-web-scraping-tutorial/

import time
import pandas as pd
import tweepy
import config_twitter

"""
consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX"    #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key
"""

consumer_key = config_twitter.API_KEY #Your API/Consumer key 
consumer_secret = config_twitter.API_KEY_SECRET #Your API/Consumer Secret Key
access_token = config_twitter.ACCESS_TOKEN    #Your Access token key
access_token_secret = config_twitter.ACCESS_TOKEN_SECRET #Your Access token Secret key


#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


username = "john"
no_of_tweets =100


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
    tweets_df.to_csv('tweets_freecc.csv')
    print(tweets_df)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
