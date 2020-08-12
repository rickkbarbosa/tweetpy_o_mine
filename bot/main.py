#!/usr/bin/env python
import sys
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
        return "Authentication OK"
    except:
        return "Error during authentication"

def get_timeline():
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

def get_userfollowers(user):
    user = api.get_user(user)

    for follower in user.followers():
        print("{} - [ @{} ]".format(follower.name, follower.screen_name))

def tweet_some(message, response=False):   
    if message is None: 
        message = "Tuitando igual seguidor de político faz (Testando robô em Python)"
    response_tweet = api.update_status(message)

    if response is True:
        return response_tweet


def search_some(text, lang="en"):
    for tweet in api.search(q=text, lang=lang, rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

#search_some("Anitta", "en")
#twitter_realtime(["Disney", "Brazil"], "en")

def main():
    api = tweepy.API(auth)  
    
    message = "Initializing my bot"
    tweet = tweet_some(message, response=True)
    api.destroy_status(tweet.id)
    since_id = tweet.id

    while True:
        try:
            print("starting from {}", format(since_id))
            since_id = check_mentions(tweet_keywords, since_id=since_id)
        except:
            print("No new tweet has found with {}",format(tweet_keywords) )
        #logger.info("Waiting...")
        time.sleep(retrieve_time)

if __name__ == "__main__":
    if len(sys.argv) > 0 :
        parameter = sys.argv[1]

        if parameter == "authentication_test":
            print(authentication_test())
            sys.exit()
        elif parameter == "search_some":
            search_some(tweet_keywords, tweet_lang)
            sys.exit()
        elif parameter == "twitter_realtime":
            twitter_realtime(tweet_keywords, tweet_lang)
        elif parameter == "tweet_some":           
            try:
                message = sys.argv[2]
                tweet_some(message)
                sys.exit()
            except:
                print("error while trying tweet")
        else:
            main()
    else:
        main()