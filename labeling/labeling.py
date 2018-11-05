#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:16:45 2018

@author: gaurav gahukar

    input file : saperation/only_songs.csv
    output file : labeling/labeled.csv


"""


import csv
import re
from textblob import TextBlob


def clean_song(song):
    song_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", song).split())
    p_song_text = ''

    for i in song_n:
        p_song_text = p_song_text + ' ' + i 

    return p_song_text


def get_sentiment(song):
    p_song_text = TextBlob(clean_song(song))             

    if p_song_text.sentiment.polarity > 0:
        return 'positive', p_song_text
    elif p_song_text.sentiment.polarity == 0:
        return 'neutral', p_song_text
    else:
        return 'negative', p_song_text
  


def main():

    fieldnames = ['sentiment_value','processed_song_text']
    writeFile = open('labeling/labeled.csv', 'w')
    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()

    with open('saperation/only_songs.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            song_text = row['text']

            sentiment_value, p_song_text = get_sentiment(song_text)

            newRow = {'sentiment_value':sentiment_value, 'processed_song_text':p_song_text}
            writer.writerow(newRow)



if __name__ == "__main__":
    main()