from __future__ import absolute_import, print_function
import tweepy
consumer_key="2NnZ6CXmo277IzPJLWLYVGZqQ"
consumer_secret="elg3HaSwxFpUpehChPQbVJim6NMS86rbb27U3mwS95jcFEjoTT"
access_token="1055158378857549824-YeRkvpBDMSibT5e9ibcKKKygKBCrUH"
access_token_secret="FkHTUwWxTJv9J9WLw6j4RvRV8MyqXHuWPniAVlIecCBUj"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(status=input("what would you like to tweet -"))
