#!/usr/bin/env python
import os

api_key = os.getenv("API_KEY")
api_secret_key = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

retrieve_time = 5
#tweet_keywords = [ "Pagode", "Samba", "Teste" ]

tweet_keywords = [ "#botdorickk" ]
phrase_file = "phrase_dict.txt"