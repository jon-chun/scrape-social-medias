# https://www.storybench.org/how-to-scrape-reddit-with-python/

import praw
import pandas as pd
import datetime as dt

import config_reddit

reddit = praw.Reddit(client_id=config_reddit.CLIENT_ID,
                     client_secret=config_reddit.CLIENT_SECRET,
                     password=config_reddit.PASSWORD,
                     user_agent=config_reddit.USER_AGENT,
                     username=config_reddit.USERNAME)

# https://praw.readthedocs.io/en/stable/getting_started/authentication.html
print(reddit.user.me())

# https://www.reddit.com/r/redditdev/comments/umppcs/getting_prawcoreexceptionsoauthexception_invalid/
# Exception has occurred: OAuthException
# invalid_grant error processing request

# https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html
subreddit = reddit.subreddit("test")
for submission in reddit.subreddit("all").hot(limit=25):
    print(submission.title)

subreddit = reddit.subreddit('Nootropics')

top_subreddit = subreddit.top()

top_subreddit = subreddit.top(limit=500)

print(type(top_subreddit))
print(len(top_subreddit))

# for submission in subreddit.top(limit=1):
#     print(submission.title, submission.id)