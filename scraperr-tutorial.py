import praw
import pandas as pd
import datetime as dt

import config_reddit


reddit = praw.Reddit(client_id=config_reddit.CLIENT_ID,
                     client_secret=config_reddit.CLIENT_SECRET,
                     user_agent=config_reddit.USER_AGENT,
                     username=config_reddit.USERNAME,
                     password=config_reddit.config_reddit.PASSWORD)
