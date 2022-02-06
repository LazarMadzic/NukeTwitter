import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline()
while (len(public_tweets)>0):
    for tweet in public_tweets:
        tweet.destroy()
    public_tweets = api.user_timeline()


public_likes=api.get_favorites()
while (len(public_likes)>0):
    for likes in public_tweets:
        likes.destroy_favorite()
    public_likes = api.get_favorites()