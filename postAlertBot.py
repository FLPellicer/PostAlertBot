#!/usr/bin/python
import praw

reddit = praw.Reddit('PostNotificationBot')

# This is the subreddit that you'll be searching your keywors on
subreddit = reddit.subreddit("watchexchange")

# These are all the possible matches that you'll be looking for
keywords = ['sbdy029', 'srpd23', 'samurai' ]

pmTitle = "Match found for "

pmBody = "A new post including one of your keywords was found! Here is the link: "

messagesBodyUrl = []

for message in reddit.inbox.messages(limit=10):
    if pmTitle in message.subject:
        messagesBodyUrl.append(message.body)
        
        
def sumbission_already_sent(submission_url):
    return any(submission.shortlink in x for x in messagesBodyUrl)

for submission in subreddit.hot(limit=50):
    #print("Title: ", submission.title)
    for keyword in keywords:
        if keyword in submission.title.lower():
            #print('There was a match!')
            is_sent = sumbission_already_sent(submission.shortlink)
            #print('Match sent: ' + str(is_sent))
            if not is_sent:
                print('Messages will be sent')
                reddit.redditor("PossibleFailure").message(pmTitle + "'" + keyword + "'", pmBody + submission.shortlink)
        break    
            
        


