#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:42:20 2019

@author: gaurav
"""


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



###############################################################################
#def for nltk Sentiment Analyser
def SentimentAnalyser(text_song):
    
    SID = SentimentIntensityAnalyzer()
    
    #s = 'madhur is a good boy'
    #s = 'sam is bad boy'
    #print(text_song)
    score = SID.polarity_scores(text_song)
    
    #print(score)
    return score

