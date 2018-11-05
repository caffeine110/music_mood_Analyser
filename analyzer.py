#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:16:45 2018

@author: gaurav
"""



import re
from textblob import TextBlob


def clean_song(song):
    song_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", song).split())
    so = ''

    for i in song_n:
        so = so + ' ' + i 

    return so


def get_sentiment(song):
    analysis = TextBlob(clean_song(song))             

    if analysis.sentiment.polarity > 0:
        print('positive')
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        print('neutral')
        return 'neutral'
    else:
        print('negative')
        return 'negative'
  


    
def main():
    song1 = "She's just my kind of girl, she makes me feel fine Who could ever believe that she could be mine?  She's just my kind of girl, without her I'm blue  And if she ever leaves me what could I do, what could I do?"

    song2 = "And when we go for a walk in the park  And she holds me and squeezes my hand  We'll go on walking for hours and talking  About all the things that we plan "

    song3 = "She's just my kind of girl, she makes me feel fine  Who could ever believe that she could be mine?  She's just my kind of girl, without her I'm blue  And if she ever leaves me what could I do, what could I do?"

    song4 = "fuck you"
    
    song5 = "thes is very bad or even wotst"


    print('for song 1 :')
    get_sentiment(song1)
    print('for song 2 :')
    get_sentiment(song2)
    print('for song 3 :')
    get_sentiment(song3)
    print('for song 4 :')
    get_sentiment(song4)
    print('for song 5 :')
    get_sentiment(song5)
    


if __name__ == "__main__":
    main()