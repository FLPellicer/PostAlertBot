#!/usr/bin/python
import praw

reddit = praw.Reddit('PostNotificationBot')

subreddit = reddit.subreddit("watchexchange")

keyword = "seiko"

url = "http://reddit.com"

pmTitle = "Match found for " + keyword

pmBody = "A new post including your keywords was found! Here is the link: "

for submission in subreddit.new(limit=10):
    print("Title: ", submission.title)
    
    if keyword in submission.title.lower():
        url = url + submission.permalink
        pmBody = pmBody + url
        reddit.redditor("PossibleFailure").message(pmTitle, pmBody)
        

    

