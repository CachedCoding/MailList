# ----------------------------------------
# Created on 3rd Apr 2021
# By the Cached Coder
# ----------------------------------------
'''
This script defines the function required
to get a PRAW object to scrape the subreddit
for the content

Borrowed from the THSB repo with modifications

Functions:
    redditLogin():
        No Inputs
        Returns API object (praw)

    getPosts(bot):
        Takes bot (praw object) as input
        and returns the top 3 posts from
        the previous day

    generateEmail(data):
        Generates the body of the email to be
        sent from the posts
'''
# ----------------------------------------
import praw
import json
# ----------------------------------------


def redditLogin():
    # Gets secrets
    with open('secrets.json', 'r') as fh:
        secrets = json.load(fh)

    # Creates an instance of the bot
    bot = praw.Reddit(
        client_id=secrets['reddit_clientid'],
        client_secret=secrets['reddit_clientse'],
        password=secrets['reddit_password'],
        user_agent=secrets['reddit_usragent'],
        username=secrets['reddit_username']
    )
    return bot


def getPosts(bot):
    # Get subreddit to scrape
    subreddit = bot.subreddit('HumansBeingBros')
    data = []
    # Loops through the submissions to scrape data from api
    submission = subreddit.top('day', limit=3)
    for post in submission:
        data.append(
            [
                post.title,
                post.permalink
            ]
        )
    return data


def generateEmail(data):
    msg = "\n"
    for post in data:
        msg += post[0] + '\nLink: https://www.reddit.com' + post[1] + '\n\n'
    # Returns the body
    return msg


if __name__ == '__main__':
    bot = redditLogin()
    data = getPosts(bot)
    body = generateEmail(data)
    print(body)
