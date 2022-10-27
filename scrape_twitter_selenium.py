
from twitter_scraper_selenium import get_profile_details
from twitter_scraper_selenium import scrape_profile

get_profile_details_fl = False
scrape_profile_fl = True

# Get Profile Details
if (get_profile_details_fl):
    twitter_username = "TwitterAPI"
    filename = "twitter_api_data"
    get_profile_details(twitter_username=twitter_username, filename=filename)

# Scrape Profile
if (scrape_profile_fl):
    microsoft = scrape_profile(twitter_username="microsoft",output_format="json",browser="firefox",tweets_count=10)
    print(microsoft)