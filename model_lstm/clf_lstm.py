#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:30:41 2019

@author: gaurav
"""


##########################################################################################
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.utils.np_utils import to_categorical


import pandas as pd
import numpy as np



##########################################################################################
def build_model(X):

    embed_dim = 128
    lstm_out = 196
    max_fatures = 2000


    model = Sequential()
    model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
    model.add(SpatialDropout1D(0.4))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(2,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
    #print(model.summary())

    return model



##########################################################################################
#from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences



##########################################################################################
# def to get sentiment
def get_Sentiment_Polarity(song_text):
    
    #print(song_text)
    df_series = pd.Series([song_text])
    df_test = pd.DataFrame(data=df_series, columns = ['lyrics'])

    max_fatures = 2000
    tokenizer = Tokenizer(num_words=max_fatures, split=' ')
    tokenizer.fit_on_texts(df_test['lyrics'])
    X = tokenizer.texts_to_sequences(df_test['lyrics'])
    X = pad_sequences(X)
    

    ##########################################################################################
    saved_model = build_model(X)
    
    
    #saved_model.load_weights('../checkpoints/Weights-003--0.41985.hdf5')
    #saved_model.load_weights('../checkpoints/Weights-002--0.68547.hdf5')
    saved_model.load_weights('/home/gaurav/Developer_repo/mmc_madhurn/deployable/model_lstm/checkpoints/Weights-003--0.68426.hdf5')
    
    
    
    ##########################################################################################
    y_pred = saved_model.predict(X)
    #y_pred = y_pred > 0.5
    print(y_pred)
    
    return y_pred


