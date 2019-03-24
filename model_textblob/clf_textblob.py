#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:16:45 2018

@author: gaurav
"""


##########################################################################################
# importing dependencies
import re
from textblob import TextBlob



##########################################################################################
# funcion to clean text_song
def clean_song(text_song):
    song_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text_song).split())
    so = ''

    # iterating through list of tokens
    for i in song_n:
        so = so + ' ' + i 

    return so




##########################################################################################
# function to get sentiment polarity
def get_Sentiment_Polarity(text_song):
    
    # creating object
    analysis = TextBlob(clean_song(text_song))             

    # get Sentiment polarity
    SentimentPolarity = analysis.sentiment.polarity

    # display origina song
    #print(text_song)

    #print(SentimentPolarity)
    return SentimentPolarity




##########################################################################################
#song = 'love me like you do good best'
#get_sentiment(song)




