# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape 
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Run the below command if you don't already have Pandas
# !pip install pandas

# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

# Below are two ways of scraping using the Python Wrapper.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
my_query = 'KariLake'
# Setting variables to be used below
maxTweets = 10

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(my_query).get_items()):
    if i>maxTweets:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into a CSV
tweets_df1.to_csv('tweets_snscrape_midjourney_20111109.csv', sep=',', index=False)


# Query by text search
my_query = 'Midjourney'
# Setting variables to be used below
maxTweets = 10

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('Midjourney since:2022-09-01 until:2022-11-09').get_items()):
    if i>maxTweets:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df2.head()

# Export dataframe into a CSV
tweets_df2.to_csv('text-query-tweets.csv', sep=',', index=False)