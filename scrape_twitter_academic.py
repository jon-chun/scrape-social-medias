# https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a

"""
Table of Contents:
1. Introduction
2. Pre-requisites to Start
3. Bearer Tokens
4. Create Headers
5. Create URL
6. Connect to Endpoint
7. Putting it all Together
8. Saving Results to CSV
9. Looping through Requests
"""

# 1. Introduction (end 2020: Twitter API v2 introduced + Academic Research Track 10M/mo, Full Archive Search > Recent 7d Search)

# 2. Pre-requisites to Start

# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata
#To add wait time between requests
import time

import pprint

# 3. Bearer Tokens

# GOTO: https://developer.twitter.com/en/portal/dashboard
# Save in config_twitter.py (add to .gitignore)

# print(json.dumps(os.environ(), indent=4))
# pprint(os.environ)

import config_twitter

consumer_key = config_twitter.API_KEY #Your API/Consumer key 
consumer_secret = config_twitter.API_KEY_SECRET #Your API/Consumer Secret Key
bearer_token = config_twitter.BEARER_TOKEN # Your API/Bearer Token
access_token = config_twitter.ACCESS_TOKEN    #Your Access token key
access_token_secret = config_twitter.ACCESS_TOKEN_SECRET #Your Access token Secret key

os.environ['TOKEN'] = bearer_token

def auth():
    return os.getenv('TOKEN')

# print(os.getenv('TOKEN'))

# 4. Create Headers

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

# 5. Create URL

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)


# 6. Connect to Endpoint

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# 7. Putting it all Together

#Inputs for the request
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "xbox lang:en"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

url = create_url(keyword, start_time,end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))


# 8. Saving Results to CSV

# 9. Looping through Requests