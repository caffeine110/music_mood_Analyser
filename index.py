#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:53:31 2019z

@author: gaurav

"""


###############################################################################
def from_nltk(song_text):
    # importng package    
    from model_nltk.clf_nltk import SentimentAnalyser
    
    # get result
    result_nltk = SentimentAnalyser(song_text)
    
    print('\nSentiment Polarity for song : ')
    
    #print('Lyrics : ',song_text)
    
    print('Using Nltk is ...')

    
    print(result_nltk)
    return result_nltk



###############################################################################
def from_textblob(song_text):
    # importing package     
    from model_textblob.clf_textblob import get_Sentiment_Polarity
    
    # get relult
    result_textblob = get_Sentiment_Polarity(song_text)
    
    print('\nSentiment Polarity for the song : ')
    
    #print('Lyrics : ',song_text)
    
    print('Using Textblob is...')

    print(result_textblob)
    return result_textblob



###############################################################################
def from_lstm(song_text):
    #importing packge
    
    from model_lstm.clf_lstm import get_Sentiment_Polarity

    result_lstm = get_Sentiment_Polarity(song_text)
    
    print('\nSentiment Polarity for song : ')
    
    #print('Lyrics : ', song_text)
    
    print('Using LSTM is ... ')
    
    print(result_lstm)
    return result_lstm



###############################################################################
def from_MNB(song_text):
    #importing packge
    
    from model_MNB.clf_MNB import get_Sentiment_Polarity

    result_MNB = get_Sentiment_Polarity(song_text)
    
    print('\nSentiment Polarity for song : ')
    
    #print('Lyrics : ', song_text)
    
    print('Using MNB is ... ')
    
    print(result_MNB)
    return result_MNB







###############################################################################
# get song text
print('Hello I am Music Mood Analyser...\n')

"""
from PyLyrics import *

lyrics = PyLyrics.getLyrics('Taylor Swift', 'Blank Space')

type(lyrics)

fileName = 'song_text.txt'

file_obj = open(fileName, 'w')
file_obj.write(lyrics)
file_obj.close()
"""

def get_Sentiment_Polarity(lyrics):
    
    #from processing import song_text
    from processing import lyrics_processing
    
    song_text = lyrics_processing(lyrics)
    
    print(song_text)
    
    
    ###############################################################################
    # Functon call to models
    
    result_nltk = from_nltk(song_text)
    
    result_textblob = from_textblob(song_text)
    
    
    result_lstm = from_lstm(song_text)
    
    result_MNB = from_MNB(song_text)
    print(result_nltk)
    print(result_textblob)
    print(result_lstm)
    print(result_MNB)
    #print(type(result_nltk))
    
    return result_nltk




lyrics = 'Love me like you do...'

res = get_Sentiment_Polarity(lyrics)
print(res)

print('\n\nExicuted Successfully...EOF...')
