## @author Valeri Kozarev
import sys
import tweepy
import Tkinter

##keys
consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

TwitterURL = ""
RedditURl = ""

def main():
    """Main entry point for the script."""
    pass

def getTopPost(url):
    "Return a link to the top post of reddit at the current hour"

def getTopComment(url):
    "Return a string representing the top comment from the top post"
    pass

def makeTweet(url):
    "post that top comment to the twitter account"
    
if __name__ == '__main__':
    sys.exit(main())