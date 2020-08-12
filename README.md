# Tweetpy O' Mine
Starts a bot to reply tweets from a specific user.

Tweet using Python (POC)

Based on original post from [RealPython.com]https://realpython.com/twitter-bot-python-tweepy/

* Create an develop account on https://developer.twitter.com/en/apps
* Create an new app and keep all 4 credentials:
* I recommend use an envfile wit the following information:

``` 
API_KEY=<the-api-key>
API_SECRET_KEY=<the-secret-key>
ACCESS_TOKEN=<the-access-token>
ACCESS_TOKEN_SECRET=<the-token-secret>

TWEET_KEYWORDS="alltweets, separated by, comma"
```


Phrase dictionary:

Tweet replies use random sentences located on _phrase_dict.txt_ . You can write your own file and mount on container.


Usage:
`
docker run -d \ 
    API_KEY=AAAAAAAAAAAAAAAAAAA \
    API_SECRET_KEY=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB \
    ACCESS_TOKEN=12345678-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
    ACCESS_TOKEN_SECRET=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb \
    TWEET_KEYWORDS="#tags, #separated, #by, #comma" \
    -d rickkbarbosa/tweetpy_o_min
`

With external phrase dictionary (and env file):
`
docker run --env-file=env_file.env \
    -v <external-phrase-dict.txt>:/bot/phrase_dict.txt
    -d rickkbarbosa/tweetpy_o_min
`