#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import re
import os

import tweepy
import time
import random
import datetime

consumer_key = consumer_key
consumer_secret = CONSUMER_SECRET_KEY
access_key = ACCESS_KEY
access_secret = ACCESS_SECRET_KEY
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

updated_status= False
def get_tweets(username):

    global updated_status


    number_of_tweets = 1


    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        if (updated_status == False) :
            tweet_status = "Device woke at " + str(datetime.datetime.now())
            status = api.update_status(status=tweet_status)

            updated_status = True

        tweet = str(tweet)

        tweetdata = re.search("'text': '(.*)', 'truncated'", tweet)
        tweetdata = tweetdata.group(1)
        if (tweetdata.find("READY FOR NEXT COMMAND") == -1):
            os.system(tweetdata)
            try:
                tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nREADY FOR NEXT COMMAND"
                status = api.update_status(status=tweet_status)
            except:
                tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nREADY FOR NEXT COMMAND " + str(random.randint(1,99999))
                status = api.update_status(status=tweet_status)               
            time.sleep(1)
        else:
            time.sleep(10)
    



while(1):
    get_tweets(USER_ID)

