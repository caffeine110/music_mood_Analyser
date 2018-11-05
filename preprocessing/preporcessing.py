"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Thu Oct  4 13:16:45 2018

@author: gaurav gahukar

    input file : saperation/only_songs.csv
    output file : labeling/labeled.csv


"""


import csv
#import re

import nltk
#import numpy as np

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

file_Path = 'preprocessing/stopwords.txt'
stop_words = set(word.strip() for word in open(file_Path))



# definations

"""
def rm_StopWords(tokens):
    tokens = [t for t in tokens if t not in stop_words]
    return tokens


def my_Lammatizer(tokens):
    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens ]
    tokens = rm_StopWords(tokens)
    return tokens
"""

def my_Tokenizer(song):
    song_text = song.lower()
    
    tokens = nltk.tokenize.word_tokenize(song_text)
    tokens = [t for t in tokens if len(t>2)]
    tokens = [wordnet_lemmatizer.lemmatize(t) for t in tokens ]
    #tokens = rm_StopWords(tokens)
    tokens = [t for t in tokens if t not in stop_words]
    #tokens = my_Lammatizer(tokens)
    
    processed_song_text = ''
    
    for t in tokens:
        processed_song_text = processed_song_text + ' ' + t
    
    return processed_song_text
  


def main():

    fieldnames = ['sentiment_value','processed_song_text']
    writeFile = open('preprocessing/preprocessed.csv', 'w')
    writer = csv.DictWriter(writeFile, fieldnames)

    with open('labeling/labeled.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            sentiment_value = row['sentiment_value']
            song_text = row['processed_song_text']

            processed_song_text = my_Tokenizer(song_text)

            newRow = {'sentiment_value':sentiment_value, 'processed_song_text':processed_song_text}
            writer.writerow(newRow)



if __name__ == "__main__":
    main()