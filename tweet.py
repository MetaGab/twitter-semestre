import tweepy
import os 
def tweet(percentage):
	consumer_key = os.environ.get('CONSUMER_KEY')
	consumer_secret = os.environ.get('CONSUMER_SECRET')
	access_token = os.environ.get('ACCESS_TOKEN')
	access_secret = os.environ.get('ACCESS_SECRET')

	status = "El semestre lleva el {}%".format(percentage)
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	api.update_with_media('bar.png', status)