import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
aquery = "covid -is:retweet place_country:US"

"""

response = client.search_recent_tweets(query=aquery, max_results=15, tweet_fields=['created_at','lang'], user_fields=['profile_image_url'], expansions=['author_id'])
users = {u['id']: u for u in response.includes['users']}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id)
        print(user.username)
        print(user.profile_image_url)

  
"""     
response = client.search_recent_tweets(query=aquery, max_results=15, tweet_fields=['created_at','lang'], user_fields=['profile_image_url'], expansions=['geo.place_id']) # author_id'])

places = {p['id']: p for p in response.includes['places']}


for tweet in response.data:
    print(tweet.id)
    if places[tweet.geo['place_id']]:
        place = places[tweet.geo['place_id']]
        print(tweet.id)
        print(place.full_name) 
        
        
file_name = 'tweets.txt'


with open(file_name, "a+") as fh:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=aquery, max_results=100).flatten(limit=1000):
        # print(tweet.id)
        fh.write(f'{tweet.id}\n')
print('bye')