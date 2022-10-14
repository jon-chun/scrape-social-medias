# https://blog.devgenius.io/scraping-reddit-with-praw-python-reddit-api-wrapper-eaa7d788d7b9
# https://github.com/Julio-M/reddit-scrape 

import config_reddit

import praw
import pandas as pd
import json

"""
r = praw.Reddit(client_id=config_reddit.CLIENT_ID,
                client_secret=config_reddit.CLIENT_SECRET,
                user_agent=config_reddit.CLIENT_USER_AGENT,
)
"""

reddit = praw.Reddit(
    client_id="FpARZIUJZE18NPZf0Wz9Qw",
    client_secret="NDQ6RKvsSgjGtm1vWPRxdlXxZo8plQ",
    password="s3cY0ndac0m",
    user_agent="testscript by u/jonc2000",
    username="jonc2000",   
)

# print(config_reddit.CLIENT_ID)
print(reddit.user.me())

"""
reddit = praw.Reddit(
    client_id=config_reddit.CLIENT_ID,
    client_secret=config_reddit.CLIENT_SECRET,
    password=config_reddit.REDDIT_PWD,
    user_agent=config_reddit.REDDIT_USER_AGENT,
    username=config_reddit.REDDIT_USERNAME,
)

print(config_reddit.CLIENT_ID)
print(reddit.user.me())


# search parameters
q='bitcoin'
sub='CryptoCurrency'
sort = "top"
limit = 50


top_posts = r.subreddit(sub).search(q, sort=sort, limit=limit)
total_posts = list()


# print(list(top_posts))


for post in top_posts:
    
    # print(vars(post)) # print all properties
    Title=post.title,
    # Score = post.score,
    # Number_Of_Comments = post.num_comments,
    # Publish_Date = post.created,
    # Link = post.permalink,
    # data_set = {"Title":Title[0],"Score":Score[0], "Number_Of_Comments":Number_Of_Comments[0],"Publish_Date":Publish_Date[0],"Link":'https://www.reddit.com'+Link[0]}

total_posts.append(data_set)



# create csv file
df = pd.DataFrame(total_posts)
df.to_csv('data.csv', sep=',', index=False)

#create json file
json_string = json.dumps(total_posts)
jsonFile = open("data.json", "w")
jsonFile.write(json_string)
jsonFile.close()

"""