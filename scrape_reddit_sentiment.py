from pprint import pprint
from re import sub
from unittest import result
from matplotlib.colors import Normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import praw
import config_reddit

user_agent = "Scraper 1.0 by /u/python_engineer"
reddit = praw.Reddit( 
                     client_id = config_reddit.CLIENT_ID,
                     client_secret = config_reddit.CLIENT_SECRET,
                     user_agent = user_agent
                     )

headlines = set()

search_term = "politics"
for submission in reddit.subreddit(search_term).hot(limit=10):
    print(submission.title)
    print(submission.id)
    print(submission.author)
    print(submission.created_utc)
    print(submission.score)
    print(submission.upvote_ratio)
    print(submission.url)
    # break
    headlines.add(submission.title)
print(len(headlines))

df = pd.DataFrame(headlines)
df.head()

dt_stamp = datetime.now().strftime("%Y%m%d-%I%M%S%p")
reddit_outfile = f'reddit_{search_term}_{dt_stamp}_praw_sentiments.csv'
df.to_csv(reddit_outfile, encoding='utf-8', index=False)

import nltk
# nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line) # -> dict
    pol_score['headline'] = line
    results.append(pol_score)
    
pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1
df.head()

df2 = df[['headline','label']]
dt_stamp = datetime.now().strftime("%Y%m%d-%I%M%S%p")
reddit_outfile = f'reddit_{search_term}_{dt_stamp}_praw_sentiments.csv'
df2.to_csv(reddit_outfile, encoding='utf-8', index=False)


df.label.value_counts()


df.label.value_counts(normalize=True)


print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("Negative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)


fig, ax = plt.subplots(figsize=(8,8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()

# frequency, tokenize, etc