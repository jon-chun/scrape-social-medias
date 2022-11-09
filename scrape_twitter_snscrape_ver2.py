from snscrape.modules import twitter 
import json 

queries = ['stable diffusion']

max_results=100

def scrape_search(query):
    scrape = twitter.TwitterSearchScraper(query)
    return scrape 

for query in queries:
    output_filename = query.replace(" ","_") + ".txt"
    with open(output_filename, 'w') as f:
        scraper = scrape_search(query)
        # i = 0
        for i, tweet in enumerate(scraper.get_items(), start=1):
            tweet_json = json.loads(tweet.json())
            print(f"\nScraped tweet #{i}: {tweet_json['content'].encode('utf8')}")
            f.write(tweet.json())
            f.write('\n')
            f.flush()
            if max_results and i > max_results:
                break
    