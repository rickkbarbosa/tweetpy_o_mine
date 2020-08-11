#!/usr/bin/env python
import tweepy
from settings import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)