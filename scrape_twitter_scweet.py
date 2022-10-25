# https://github.com/Altimis/Scweet

# pip install Scweet==1.8

from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

data = scrape(hashtag="bitcoin", since="2021-08-05", until=None, from_account = None, interval=1, 
              headless=True, display_type="Top", save_images=False, 
              resume=False, filter_replies=True, proximity=True)

print(type(data))