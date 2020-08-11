#!/usr/bin/env python
import tweepy
from settings import *
from twitter_authentication import *
from tweet_on_realtime import *

api = tweepy.API(auth)

def authentication_test():
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

def get_timeline():
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")


def get_userfollowers(user):
    user = api.get_user(user)

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)

    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)


def tweet_some(message):
    if message is None: 
        message = "Tuitando igual seguidor de político faz (Testando robô em Python)"
    api.update_status(message)

def search_some(text, lang="en"):
    for tweet in api.search(q=text, lang=lang, rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

message = "Postando uma groselha qualquer"
tweet_some(message)
#search_some("Anitta", "en")
#twitter_realtime(["Disney", "Brazil"], "en")