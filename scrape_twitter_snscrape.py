# https://www.freecodecamp.org/news/python-web-scraping-tutorial/
# https://github.com/Altimis/Scweet/blob/master/Example.ipynb

import snscrape.modules.twitter as sntwitter
# https://github.com/Altimis/Scweet
# 
import pandas as pd

from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

"""
# Search by Keywords
data = scrape(words=['dalle2','midjourney'], since="2021-10-20", until="2021-10-26", 
              from_account = None, interval=1, headless=False, display_type="Top", 
              save_images=False, lang="en", resume=False, filter_replies=False, 
              proximity=False, geocode="38.3452,-0.481006,200km")
              
data.head()
"""

# Search by Hashtags
data = scrape(hashtag="dalle2", since="2021-10-20", until=None, from_account = None, interval=1, 
              headless=True, display_type="Top", save_images=False,
              # show_images=True, save_images=True,
              resume=False, filter_replies=True, proximity=True)
data.head()

"""
# Get User Info
users = ['nagouzil', '@yassineaitjeddi', 'TahaAlamIdrissi', 
         '@Nabila_Gl', 'geceeekusuu', '@pabu232', '@av_ahmet', '@x_born_to_die_x']

users_info = get_user_information(users, headless=True)
users_info.head()
"""

"""
# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:john').get_items()):
    if i>10:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])

tweets_df.to_csv('tweets_snscrape.csv')
print(tweets_df)

"""