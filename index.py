#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:53:31 2019

@author: gaurav

"""


###############################################################################
def from_nltk(text_song):
    # importng package    
    from model_nltk.clf_nltk import SentimentAnalyser
    
    # get result
    result_nltk = SentimentAnalyser(text_song)
    
    print('\nSentiment Polarity for song : ')
    print('Lyrics : ',text_song)
    print('Using Nltk is ...')

    
    print(result_nltk)
    return result_nltk



###############################################################################
def from_textblob(text_song):
    # importing package     
    from model_textblob.clf_textblob import get_Sentiment_Polarity
    
    # get relult
    result_textblob = get_Sentiment_Polarity(text_song)
    
    print('\nSentiment Polarity for the song : ')
    print('Lyrics : ',text_song)
    print('Using Textblob is...')

    print(result_textblob)
    return result_textblob




###############################################################################
# get song text
print('Hello I am Music Mood Analyser...\n')

song_text = 'Love me like you do'





###############################################################################
# Functon call to models
result_nltk = from_nltk(song_text)

result_textblob = from_textblob(song_text)



print('\n\nExicuted Successfully...EOF...')