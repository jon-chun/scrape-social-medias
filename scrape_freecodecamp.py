# Two forms of Scraping Twitter: Tweepy vs SNScrape
# 
# # https://www.freecodecamp.org/news/python-web-scraping-tutorial/
# Jon Chun
# 21 Oct 2022

import time
import pandas as pd
import tweepy
import config_twitter


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


username = "elonmusk"
no_of_tweets = 10


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
    
    tweets_df.to_csv('tweets_10_elonmusk_20221021_1300.csv')