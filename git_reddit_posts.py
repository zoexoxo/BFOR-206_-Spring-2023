# This script will use praw to get posts from reddit

#%% imports

import os
import praw
from dotenv import load_dotenv
import pandas as pd

#%% load credentials

# store API credntials
load_dotenv()
APP_ID = os.environ.get('APP_ID')
API_SECRET = os.environ.get('API_SECRET')
print('APP_ID:\t\t', APP_ID)
print('API_SECRET:\t', API_SECRET)

#%% connect to reddit

def reddit_connection():
    reddit = praw.Reddit(client_id=APP_ID,
        client_secret=API_SECRET,
        user_agent= 'Post Downloader')
    print('Successful app authentification', reddit.read_only)

    return reddit

# Typehint(->) tells you what should be returned
def get_submissions(reddit, subreddit, limit=10) -> pd.DataFrame:
    
    #this function will get posts from a subreddit and return then as a data frame
    submissions = reddit.subreddit(subreddit).top(limit=limit)

#add list to master list
    df_rows = []
    for submission in submissions:
        print(submission.id)
        #print([submission.author.name])
       
       #if user ha deleted their account
        if not hasattr(submission.author, 'name'):
            print('found deleted user')
            author_name = '[deleted]'
        else:
            author_name = submission.author.name

       
        df_rows.append([submission.id, submission.score, submission.title, submission.num_comments, submission.subreddit.display_name, author_name, submission.created_utc, submission.selftext])

    post_df = pd.DataFrame(df_rows,columns=['id', 'score', 'title', 'num_comments','subreddit.display_name','author', 'created_utc', 'selftext'])

    return post_df

def create_submission_df(submissions: praw.reddit.Submission) -> pd.DataFrame:
	"""
	This function will create a dataframe from a list of submissions.
	"""

	df_rows = []
	for submission in submissions: # type: ignore
		# print(submission.id)
		# print([submission.author.name])

		"""
		If the user has deleted their account, there 
		will not be any value for the author name. We 
		will replace this with the name [deleted].
		"""
		if not hasattr(submission.author, 'name'):
			print('found deleted user')
			author_name = '[deleted]'
		else:
			author_name = submission.author.name

		df_rows.append([submission.id, submission.score, submission.title, submission.num_comments, submission.subreddit.display_name, author_name, submission.created_utc, submission.selftext])

	post_df = pd.DataFrame(df_rows, columns=['id', 'score', 'title', 'num_comments', 'subreddit', 'author', 'created_utc', 'selftext'])

	return post_df

def get_comments_from_post(reddit, post_id) -> pd.DataFrame:



#this function will return a dataframe of comments for a post
#get the submission
    submission = reddit.submission(id=post_id)

    #get a list of comments
    submission.comments.replace_more(limit=0)
    comments_list = submission.comments.list()

    comment_rows = []
    for comment in comments_list:
        #if user has deleted their account
        if not hasattr(comment.author, 'name'):
            print('found deleted user')
            author_name = '[deleted]'
        else:
            author_name = comment.author.name

        comment_rows.append([comment.id, comment.score, comment.created_utc, comment.body, comment.parent_id, author_name, comment.subreddit.display_name])

    comments_df = pd.DataFrame(comment_rows, columns=['id','score', 'created_utc','body','parent_id', 'author','subreddit'])

    return comments_df

#%% test for our function

if __name__ == '__main__':
    #authentification function
    reddit = reddit_connection()

    # check the get submission function
    submission_df = get_submissions(reddit, 'cybersecurity')

    #check the comments dataframe function
    comments_df = get_comments_from_post(reddit, post_id='120j74c')

    print(comments_df.shape)


    # %% read the list of subreddits

    #read the list of subreddits from a txt file
    with open('subreddit_list.txt', 'r') as f:
        subreddits = f.read().splitlines()

    #%% get the top 100 post from each subreddit

    submission_df_list = []

    for sr in subreddits:
        print(sr)
        submission_df_list.append(get_submissions(reddit, sr, 100))
    # %% concatenate the dataframes

    submission_df = pd.concat(submission_df_list)

    # %% 100 posts

    posts_ids = submission_df['id'].sample(10).to_list()


    # %% get comments for posts

    comment_df_list = []

    for posts in posts_ids:
        print('working on', posts)
        comment_df_list.append(get_comments_from_post(reddit, posts))

    # %% concatenate all commentrs into one df

    comments_df = pd.concat(comment_df_list)
    # %% write data into csv

    comments_df.to_csv('Data/comments_df_10.csv')
    # %% write data submissions into csv

    submission_df.to_csv('Data/submission_df_10.csv')

    
