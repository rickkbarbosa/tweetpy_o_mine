#!/usr/bin/env python
import os

api_key = os.getenv("API_KEY")
api_secret_key = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

retrieve_time = 60

#tweet_keywords = [ "Pagode", "Samba", "Teste" ]
tweet_keywords = os.getenv("TWEET_KEYWORDS")
tweet_keywords = [i.strip() for i in tweet_keywords.split(',')]

phrase_file = "phrase_dict.txt"