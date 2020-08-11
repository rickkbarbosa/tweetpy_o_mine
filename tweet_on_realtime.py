#!/usr/bin/env python
import tweepy
import json
from settings import *
from twitter_authentication import *


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


def twitter_realtime(text, lang="en"):
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=text, languages=[lang])
