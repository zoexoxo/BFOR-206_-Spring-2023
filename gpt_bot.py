#This script will be used to send prompts to the 
#GPT API and post the replies to reddit.

# %% imports

import os
import openai
from dotenv import load_dotenv
import git_reddit_posts as grp


# %%

# store API credntials
load_dotenv()
openai.api_key = os.environ.get('OPEN_AI')
openai.Model.list()

def find_relevant_posts(submissions_df):

  

  #Find posts that seem good to respond to.
  #You can adjust your criteria to choose what you like.
  #This could be based on score, keywords, etc.

  # sort by newest
  top_post = submissions_df.sort_values(by='created_utc',ascending=False).head(1)

  return top_post

def prompt_gpt(prompt: str):

  #Generate a response to a prompt

  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": prompt}])
  return completion.choices[0].message

def has_ai_language(response: str) -> bool:
  #This function will check if the response contains the "As an AI launguage model" disclaimer

  check_string = "as an AI language model".lower()

  if check_string in response.lower():
    return True
  
  else:
    return False
  
  # check ai language function

def test_has_ai_language():

  assert True == has_ai_language("As an AI language model, I don't have personal opinons.")
  assert False == has_ai_language("I don't have personal opinons,")

def update_post_history(post_id: str, history_file: str):
  #This function will uodate the post hsitory with the post that was responded to
  #If the post id is already in the file


  #check for post id in file
  with open(history_file, 'r') as f:
    post_ids = f.readlines()

  #check if post id is in file
  if post_id in post_ids:
    print("Post has already been responded to")
    return True
  
  #add post id to file
  with open(history_file, 'a') as f:
    f.write(post_id + '\n')
    return False
  
  


#%% main
if __name__ == '__main__':

  print('Running GPT bot')

  reddit = grp.reddit_connection()

  #get posts
  submissions = reddit.subreddit('AskReddit').hot(limit=5)
  
  # this function is a simpler version of what we had earlier
  submissions_df = grp.create_submission_df(submissions)

  top_post = find_relevant_posts(submissions_df)
  
  # check if there are any post to respond to
  for index, submission in top_post.iterrows():
    print

  
  prompt = top_post['title'].values[0]
  
  response = prompt_gpt(prompt)
  
  print("Prompt: ", prompt)
  
  print("Response: ", response)

#%%
# test the check_post_history function
def test_check_post_history():
  assert True == check_post_history('test1', 'data/post_history.txt')



