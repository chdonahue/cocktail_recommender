# This script creates a dictionary for a selection of spirits based on ones that have a subreddit. This is used 
# for training a model for classification
import dill
import praw
import os
import simplejson as json
from praw.models import MoreComments

# A selection of the most common spirits found as mixers in cocktails:
spirit_list = ['bourbon','brandy', 'gin', 'mezcal','rum', 'tequila', 'vodka', 'whiskey','cachaca','absinthe']


with open("secrets/reddit_secrets.json.nogit") as fh:
    secrets = json.loads(fh.read())


reddit = praw.Reddit(
    user_agent="drinkbot 5000",
    client_id = secrets['CLIENT_ID'],
    client_secret = secrets['CLIENT_SECRET'],
    username= secrets['USERNAME'],
    password= secrets['PASSWORD']
)


# Take the top 1000 posts for each subreddit and store in a dictionary
def create_comment_list(sub): # Takes sub
    """
    Takes subreddit string (sub) and generates a list of text: 1 for each post.
    Returns list of comments
    """
    subreddit = reddit.subreddit(sub)
    comments = []
    for submission in subreddit.top(limit=1000):
        this_post = '' # current post. 
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            this_post += top_level_comment.body

        comments.append(this_post)
    return comments


# Create a dictionary of comments for each spirit:
d = {}
for spirit in spirit_list:
    print('scraping '+spirit)
    L = create_comment_list(spirit)
    d[spirit] = L
    



if not os.path.exists('model_data'):
	os.mkdir('model_data')

dill.dump(d, open('model_data/reddit_spirits.pkd', 'wb'))

