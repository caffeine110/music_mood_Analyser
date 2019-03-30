#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:25:39 2019

@author: gaurav
"""


import numpy as np
import pandas as pd
import re

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences



##########################################################################################
data = pd.read_csv('../data/train_lyrics_1000.csv')
print(data.columns)
# Keeping only the neccessary columns
data = data[['lyrics','mood']]

#print(type(data))
print(data.columns)
#print(data.head(10))



##########################################################################################
#data = data[data.sentiment != "Neutral"]
data['lyrics'] = data['lyrics'].apply(lambda x: x.lower())
data['lyrics'] = data['lyrics'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))
data['lyrics'] = data['lyrics'].apply((lambda x: x.replace('\n', ' ')))

#data['lyrics'] = data['lyrics'].replace('\n', ' ')


print(data.head(10))

print(data[ data['mood'] == 'happy'].size)
print(data[ data['mood'] == 'sad'].size)

data = data.dropna()

print(data[ data['mood'] == 'happy'].size)
print(data[ data['mood'] == 'sad'].size)




##########################################################################################
max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['lyrics'].values)
X = tokenizer.texts_to_sequences(data['lyrics'].values)
X = pad_sequences(X)

type(X)




##########################################################################################
Y = pd.get_dummies(data['mood']).values
print(Y)


##########################################################################################
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.1, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


