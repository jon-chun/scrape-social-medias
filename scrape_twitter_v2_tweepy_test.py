import tweepy
import config_twitter

client = tweepy.Client(bearer_token=config_twitter.BEARER_TOKEN)

query1_fl = False
query2_fl = False
query3_fl = True

# Query #1
if query1_fl:
    my_query = 'midjourney prompt -is:retweet has:media'

    response = client.search_recent_tweets(query=my_query, user_fields=['profile_image_url'], tweet_fields=['created_at','lang'], expansions=['author_id'])

    users = {u['id']: u for u in response.includes['users']}

    for tweet in response.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
            print(tweet.id)
            print(user.username)
            print(user.profile_image_url)

# Query #2
if query2_fl:
    my_query = 'midjourney prompt -is:retweet has:media place_country:us'

    response = client.search_recent_tweets(query=my_query, tweet_fields=['created_at','lang'], expansions=['author_id'])`

    for tweet in response.data:
        # user = users[tweet.author_id]
        print(tweet.id)
        # print(user.username)
        # print(user.profile_image_url)
    
# Query #3
if query3_fl:
    my_query = 'midjourney prompt -is:retweet has:media place_country:us'

    response = client.search_recent_tweets(query=my_query, tweet_fields=['created_at','lang'], expansions=['geo.place_id'])

    places = {p['id']:p for p in response.includes['places']}
    
    for tweet in response.data:
        print(tweet.id)
        if places[tweet.geo['place_id']]:
            place = places[tweet.geo['place_id']]
            # print(tweet.id)
            print(place.full_name)
        # user = users[tweet.author_id]
        print(tweet.id)
        # print(user.username)
        # print(user.profile_image_url)