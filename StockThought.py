## @author Valeri Kozarev
import sys
import time
import praw
import tweepy
import random

##twitter keys
twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_token_secret = ''

def main():
    while True:
        top_comment = getTopComment()
        makeTweet(top_comment)
        time.sleep(60)      ##run every 30 minutes

def getTopComment():
    ##connect to subreddit
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         user_agent='')

    ##choose one of our subreddits at random
    subreddit_list = ["stocks", "options", "wallstreetbets", "stockmarket", "robinhood", "investing"]
    subreddit_title = random.choice(subreddit_list)
    subreddit = reddit.subreddit(subreddit_title)

    ##get the top post
    for submission in subreddit.hot(limit=5):
        if submission.locked or submission.stickied:
            continue
        for comment in submission.comments:
            if hasattr(comment, "body") and comment.distinguished==None:
                top_comment = comment.body
                ##store top comment that matches all our criteria
                if (len(top_comment) <= 280 and top_comment != "[removed]"):
                    return top_comment
        
        return None


def makeTweet(comment):
    ##authorization for Twitter
    twitter_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    twitter_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    twitter_api = tweepy.API(twitter_auth)

    ##make tweet
    try:
        twitter_api.update_status(comment)
        print("new tweet")
    except tweepy.error.TweepError as e:
        print("Caught an error, message below:")
        print(e.reason)
    return
    
if __name__ == '__main__':
    sys.exit(main())
