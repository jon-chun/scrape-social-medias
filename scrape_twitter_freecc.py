# https://www.freecodecamp.org/news/python-web-scraping-tutorial/

import time
import pandas as pd
import tweepy
import config_twitter
from datetime import datetime
import unicodedata

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
    print(tweets_df.columns)
    # tweets_df.Tweet = tweets_df.Tweet.apply(lambda x: x.encode('unicode-escape').decode('utf-8')))
    
    tweets_df['Tweet'] = tweets_df['Tweet'].apply(lambda x: unicodedata.normalize('NFD', x).encode('ascii', 'ignore'))
    dt_stamp = datetime.now().strftime("%Y%m%d-%I%M%S%p")
    tweets_outfile = f'tweets_{username}_{dt_stamp}_freecc.csv'
    print(f'Output filename: {tweets_outfile}')
    tweets_df.to_csv(tweets_outfile, encoding='ISO-8859-1', errors='ignore')
    # tweets_df.to_csv(tweets_outfile, encoding='utf-8', errors='ignore')
    print(tweets_df)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)
