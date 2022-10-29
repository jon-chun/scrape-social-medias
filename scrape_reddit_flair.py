# https://www.kaggle.com/code/dillontate/reddit-scraper

# Reddit Module to abstract the task of data abstraction 

# Import PRAW - python reddit API wrapper
!pip install praw
!pip install pandas
import praw
import pandas as pd

# Data features that we will be collecting 
features = [
    'ID', 
    'is_Original', 
    'Flair',
    'num_comments', 
    'Title',
    'Subreddit', 
    'Body', 
    'URL', 
    'Upvotes',
    'created_on', 
    'Comments'
]

# Function to authenticate the user 
def reddit_auth(my_client_id, my_client_secret, user):
    '''
    INPUTS: 
    
    my_client_id: generated from the Reddit app website
    my_client_secret: generated from the Reddit app website
    user_agent: generated from the Reddit app website

    OUTPUT: 

    dataframe with the complete data 
    '''
    
    reddit_auth_var = praw.Reddit(client_id=my_client_id, 
                        client_secret=my_client_secret, 
                        user_agent=user)

    print("Created a Reddit instance with the following details:")
    print("Client ID: {}\nUser Agent:: {}".format(my_client_id, user))

    # Return the instance 
    return reddit_auth_var


# Function to get the unique flairs 
def get_unique_flairs(reddit, sub_name, num_posts):
    
    '''
    INPUTS: 

    reddit: An instance of the Reddit API
    subreddit: the subreddit the post belongs to 
    num_posts: Number of posts to look for 

    OUTPUT: 

    dataframe with the complete data 

    '''
    # Getting post data
    posts = reddit.subreddit(sub_name).top(limit=num_posts)
    # url = "https://www.reddit.com/r/Games/comments/q9v3mh/weekly_rgames_discussion_what_have_you_been/"
    # posts = reddit.submission(url=url)
    
    # Collect a unique list of flairs 
    flairs = []
    for post in posts:

        # Extract flair name
        post_flair = post.link_flair_text
        if post_flair != None: 

            # Check if flair in the list 
            # Add if not
            if post_flair not in flairs:
                flairs.append(post_flair)
    
    # Check if not empty 
    if len(flairs) != 0: 
        return flairs
    
    else:
        print("No Flairs found.")
        return 0


# Function to get the data using particular flairs
def scrape_with_flairs(reddit, sub_name, flairs, num_per_flair, features=features, comments=True):
    
    '''
    INPUTS: 

    reddit: An instance of the Reddit API
    subreddit: the subreddit the post belongs to 
    flairs: list of flairs that you need the data for
    num_per_flair: Number of posts per flair 
    comments: True if you want additional comments and False if you 

    OUTPUT: 

    dataframe with the complete data 

    '''
    
    # Get comments detail 
    if comments == True:
        comment_limit = None
    else: 
        comment_limit = 0
    
    
    # Create a list which will have each row as an entry  
    posts = []
    
    # Create a subreddit instance 
    subreddit_total = reddit.subreddit(sub_name)

    # Top posts of each flair type based on the number of posts per flair 
    for flair in flairs: 
        
        print("Collecting for flair: {}".format(flair))
        relevant_subs = subreddit_total.search(f"flair_name:{flair}", limit=num_per_flair)

        for sub in relevant_subs:
            post = []
            post = [
                str(sub.id),
                sub.is_original_content,
                str(sub.link_flair_text),
                sub.num_comments,
                str(sub.title),
                str(sub.subreddit),
                str(sub.selftext),
                str(sub.url),
                sub.score,
                sub.created_utc,
            ]
            
            # Collect comments
            sub.comments.replace_more(limit=None)
            comment = ''
            for top_comment in sub.comments:
                comment = str(top_comment.body) + ' '        

            post.append(str(comment))# Add to the end of the list 
            posts.append(post)    # Add to the main list

            # Update after every 100 posts
            if len(posts) % 100 == 0:
                print("Number of posts collected: {}".format(len(posts)))
   
    # Convert to a data frame 
    posts_df = pd.DataFrame(posts, columns=features)
    print("The size of the collected dataframe is: {}".format(posts_df.shape))
    
    # Using the to_datetime function of pandas to convert time from UNIX to regular 
    posts_df['creation_date'] = pd.to_datetime(posts_df['created_on'], dayfirst=True, unit='s')
    # Drop created_on column now 
    posts_df.drop(['created_on'], axis=1, inplace=True)
    
    # Return the dataframe
    return posts_df

# Function to collect data without flairs
def scrape_without_flairs(reddit, sub_name, num_posts, features=features, comments=True):
    
    '''
    INPUTS: 

    reddit: An instance of the Reddit API
    subreddit: the subreddit the post belongs to 
    num_posts: Number of posts
    comments: True if you want additional comments and False if you 

    OUTPUT: 

    dataframe with the complete data 

    '''
    
    # Get comments detail 
    if comments == True:
        # comment_limit = None
        comment_limit = 50
    else: 
        comment_limit = 0
    
    print("Started Collecting Data!")
    
    # Create a list which will have each row as an entry  
    posts = []
    sublist = []
    comment_list = []
    
    # Tag the post we want data from
    url = "https://www.reddit.com/r/Games/comments/q9v3mh/weekly_rgames_discussion_what_have_you_been/"
    sub1 = reddit.submission("q9v3mh")
    sublist.append(sub1)
    sub2 = reddit.submission("q54fso")
    sublist.append(sub2)
    sub3 = reddit.submission("q0e57v")
    sublist.append(sub3)
    sub4 = reddit.submission("pvq7di")
    sublist.append(sub4)
    sub5 = reddit.submission("pr4gmp")
    sublist.append(sub5)
    sub6 = reddit.submission("pmpbcg")
    sublist.append(sub6)
    
    # Create a subreddit instance 
    # subreddit_total = reddit.subreddit(sub_name)

    # Loop through each subreddit entry and append that to the posts list
    '''
    for sub in subreddit_total.top(limit=num_posts):
    '''    
    for sub in sublist:
        # Empty list to append post data 
        post = []

        post = [
            str(sub.id),
            sub.is_original_content,
            str(sub.link_flair_text),
            sub.num_comments,
            str(sub.title),
            str(sub.subreddit),
            str(sub.selftext),
            str(sub.url),
            sub.score,
            sub.created_utc,
        ]
        
        
        # print if post data was successfully read
        print("Post data read")
        
        # Collect comments
        sub.comments.replace_more(limit=comment_limit)
        comment = ''
        
        #for top_comment in sub.comments:
        #    comment = str(top_comment.body) + ' '  
            
        for top_comment in sub.comments:
            comment = str(top_comment.body) + ' '
            comment_list.append(comment)
            
        # comment data printing
        # print(post)
    
        post.append(str(comment))# Add to the end of the list 
        posts.append(post)    # Add to the main list
        
        # Update after every 100 posts
        if len(posts) % 100 == 0:
            print("Number of posts collected: {}".format(len(posts)))
   
    # Convert to a data frame 
    posts_df = pd.DataFrame(posts, columns=features)
    print("The size of the collected dataframe is: {}".format(posts_df.shape))
    
    # Using the to_datetime function of pandas to convert time from UNIX to regular 
    posts_df['creation_date'] = pd.to_datetime(posts_df['created_on'], dayfirst=True, unit='s')
    # Drop created_on column now 
    posts_df.drop(['created_on'], axis=1, inplace=True)
    
    # Return the dataframe and list of comments
    return posts_df, comment_list


# Main code to run the Web Scraper
reddit_instance = reddit_auth("Vu3sWAZl4FCASbG-b48yVA","c9DP0SnvdxxGDlcGbZ6ecjt7YLTsOg","Kaggle Scraping")
reddit_dataframe, comment_list = scrape_without_flairs(reddit_instance, "games", 3)
reddit_dataframe.to_csv('reddit_data.csv')

comment_dataframe = pd.DataFrame(data={"Comment Body": comment_list})
comment_dataframe.to_csv("Comment Data.csv", sep=',',index=False)
# print test
#print("Run complete")
#print("Comment list: ")
#count = 1
#for comment in comment_list:
#    print("----------Comment " + str(count) + "----------\n" + comment)
#    count = count + 1