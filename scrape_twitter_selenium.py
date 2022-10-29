# https://github.com/shaikhsajid1111/twitter-scraper-selenium

# FIX: https://stackoverflow.com/questions/73861078/scrapy-attributeerror-module-openssl-ssl
# PyOpenSSL 21.0.0 => 22.0.0

import pandas as pd
from datetime import datetime

from twitter_scraper_selenium import scrape_profile
from twitter_scraper_selenium import get_profile_details
from twitter_scraper_selenium import scrape_keyword_with_api



keyword_username = 'elonmusk'
keyword_search = '#dalle2'
max_tweet_ct = 10

get_profile_fl = False
get_profile_details_fl = False
get_tweets_keyword_fl = False

dt_stamp = datetime.now().strftime("%Y%m%d-%I%M%S%p")

# Scrape user details (Fast)
if get_profile_details_fl:
    filename_out = f'twitter_{keyword_username}_{dt_stamp}_profile-details'
    print(f'Scraping profile-details info into file: {filename_out}')
    get_profile_details(twitter_username=keyword_username, filename=filename_out)
    # print(f"\n\n{aprofile_details}\n\n")
    print(f'Profile info saved to: {filename_out}')
    
# Scrape user tweets (Slow)
if get_profile_fl:
    filename_out = f'twitter_{dt_stamp}_{keyword_username}_profile'
    print(f'Scraping profile info into file: {filename_out}')
    scrape_profile(twitter_username=keyword_username,
                              filename=filename_out,
                              output_format="csv",
                              browser="firefox",
                              tweets_count=max_tweet_ct)
    # print(f"\n\n{aprofile}\n\n")
    print(f'Profile info saved to: {filename_out}')
    
# Scrape user with keywords using API
if get_tweets_keyword_fl:
    filename_out = f'twitter_{dt_stamp}_keyword_{keyword_search}'
    print(f'Scraping profile for tweets containing [{keyword_search}] into file: {filename_out}')
    scrape_keyword_with_api(query=keyword_search, 
                            tweets_count=max_tweet_ct, 
                            output_filename=filename_out)
    
from twitter_scraper_selenium import scrape_keyword_with_api

query = "#gaming"
tweets_count = 10
output_filename = "gaming_hashtag_data"
scrape_keyword_with_api(query=query, tweets_count=tweets_count, output_filename=output_filename)
