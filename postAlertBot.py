#!/usr/bin/python
import praw

reddit = praw.Reddit('PostNotificationBot')

subreddit = reddit.subreddit("watchexchange")

keyword = "seiko"

url = "http://reddit.com"

pmTitle = "Match found for " + keyword

pmBody = "A new post including your keywords was found! Here is the link: "

messagesBodyUrl = []

def sumbission_already_sent(url):
    for message in messagesBodyUrl:
        if url in message:
            print('message repeated, will not send')
            return bool(True)
        else: 
            return bool(False)
        

for message in reddit.inbox.messages(limit=10):
    if pmTitle in message.subject:
        messagesBodyUrl.append(message.body)

for submission in subreddit.new(limit=10):
    print("Title: ", submission.title)
    
    if keyword in submission.title.lower():
        url = url + submission.permalink
        is_sent = sumbission_already_sent(url)
        if not is_sent:
            print('Messages will be sent')
            pmBody = pmBody + url
            reddit.redditor("PossibleFailure").message(pmTitle, pmBody)
        


