# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Recent-Search/recent_search.py

import requests
import os
import json

import config_twitter

consumer_key = config_twitter.API_KEY #Your API/Consumer key 
consumer_secret = config_twitter.API_KEY_SECRET #Your API/Consumer Secret Key
bearer_token = config_twitter.BEARER_TOKEN # Your API/Bearer Token
access_token = config_twitter.ACCESS_TOKEN    #Your Access token key
access_token_secret = config_twitter.ACCESS_TOKEN_SECRET #Your Access token Secret key

os.environ['BEARER_TOKEN'] = bearer_token

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "http://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','max_results': 10, 'tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

search_url = ""
query_params = ""

json_response = connect_to_endpoint(search_url, query_params)
print(json.dumps(json_response, indent=4, sort_keys=True))
