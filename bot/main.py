#!/usr/bin/env python
import tweepy
from settings import *
from twitter_authentication import *
from twitter_autoreply import *
from tweet_on_realtime import *

def phrase_dict():
    global phrase_dict
    file = open(phrase_file, 'r')
    phrase_dict = file.readlines()
    file.close() 

    return phrase_dict

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

    for follower in user.followers():
        print("{} - [ @{} ]".format(follower.name, follower.screen_name))

def tweet_some(message):
    if message is None: 
        message = "Tuitando igual seguidor de político faz (Testando robô em Python)"
    api.update_status(message)

def search_some(text, lang="en"):
    for tweet in api.search(q=text, lang=lang, rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

#message = "Postando uma groselha qualquer"
#tweet_some(message)
#search_some("Anitta", "en")
#twitter_realtime(["Disney", "Brazil"], "en")

def main():
    api = tweepy.API(auth)  
    since_id = 1293300000000000000
    while True:
        try:
            since_id = check_mentions(tweet_keywords, since_id=since_id)
        except:
            print("No new tweet has found with {}",format(tweet_keywords) )
        #logger.info("Waiting...")
        time.sleep(retrieve_time)

if __name__ == "__main__":
    main()