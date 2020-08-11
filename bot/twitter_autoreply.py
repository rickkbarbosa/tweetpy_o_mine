#!/usr/bin/env python
import tweepy
import logging
import time
import random
from settings import *
from twitter_authentication import *
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger()

def check_mentions(keywords, since_id):
    #logger.info("Retrieving mentions")

    file = open(phrase_file, 'r')
    phrase_dict = file.readlines()
      
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id ).items():
        if tweet.in_reply_to_status_id is not None:
            print("Não encontrei ninguém com {}", format(tweet_keywords))
            continue
        if any(keyword in tweet.text.lower() for keyword in tweet_keywords):
            print("Tem nesse: {}", format(tweet.text) )
            print("{}", format(random.choice(phrase_dict)))

            # if not tweet.user.following:
            #     tweet.user.follow()

            try:
                api.update_status(
                    status="@{} {}".format(tweet.user.screen_name, random.choice(phrase_dict)),
                    in_reply_to_status_id=tweet.id,
                )
            except:
                print("Fail for some reason")
    return tweet.id