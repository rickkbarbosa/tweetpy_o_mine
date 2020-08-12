# tweetpy_o_mine
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

Usage:

`
docker run --env-file=env_file.env -d rickkbarbosa/tweetpy_o_min
`