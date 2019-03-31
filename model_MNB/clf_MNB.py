#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:34:46 2019

@author: gaurav
"""

##########################################################################################
import pandas as pd



##########################################################################################
df = pd.read_csv('/home/gaurav/Developer_repo/mmc_madhurn/deployable/model_MNB/data/train_lyrics_1000.csv')


##########################################################################################
from sklearn.preprocessing import LabelEncoder

X_train = df['lyrics'].values 

y_train = df['mood'].values


le = LabelEncoder()
le.fit(y_train)
y_train = le.transform(y_train)



##########################################################################################
# Save object to disk
"""
import pickle
pickle_out = open('/home/gaurav/Developer_repo/mmc_madhurn/deployable/model_MNB/model/files/lyrics_label_encoder_py.pkl', 'wb')
pickle.dump(le, pickle_out)
pickle_out.close()
"""


##########################################################################################
# Porter Stemmer

import nltk
import re

porter_stemmer = nltk.stem.porter.PorterStemmer()

def porter_tokenizer(text, stemmer=porter_stemmer):
    """
    A Porter-Stemmer-Tokenizer hybrid to splits sentences into words (tokens) 
    and applies the porter stemming algorithm to each of the obtained token. 
    Tokens that are only consisting of punctuation characters are removed as well.
    Only tokens that consist of more than one letter are being kept.
    
    Parameters
    ----------
        
    text : `str`. 
      A sentence that is to split into words.
        
    Returns
    ----------
    
    no_punct : `str`. 
      A list of tokens after stemming and removing Sentence punctuation patterns.
    
    """
    lower_txt = text.lower()
    tokens = nltk.wordpunct_tokenize(lower_txt)
    stems = [porter_stemmer.stem(t) for t in tokens]
    no_punct = [s for s in stems if re.match('^[a-zA-Z]+$', s) is not None]
    return no_punct




##########################################################################################    
with open('/home/gaurav/Developer_repo/mmc_madhurn/deployable/model_MNB/data/stopwords_eng.txt', 'r') as infile:
    stop_words = infile.read().splitlines()

#print('stop words %s ...' %stop_words[:5])



##########################################################################################
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
            encoding='utf-8',
            decode_error='replace',
            strip_accents='unicode',
            analyzer='word',
            binary=False,
            stop_words=stop_words,
            tokenizer=porter_tokenizer
    )




##########################################################################################
#vocab = ["try to get vocab from this sentence "]
#tfidf = tfidf.fit(vocab)


##########################################################################################
tfidf = tfidf.fit(X_train.ravel())
#print('Vocabulary size: %s' %len(tfidf.get_feature_names()))






##########################################################################################
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline



##########################################################################################
final_clf = Pipeline([
                ('vect', TfidfVectorizer(
                                         binary=False,
                                         stop_words=stop_words,
                                         tokenizer=porter_tokenizer,
                                         ngram_range=(1,1),
                                         )
                ),
                ('clf', MultinomialNB(alpha=1.0)),
               ])
    
    

    
    
##########################################################################################    
history = final_clf.fit(X_train, y_train)



df_test = pd.DataFrame()
def get_Sentiment_Polarity(song_text):
    df_series = pd.Series([song_text])
    df_test = pd.DataFrame(data=df_series, columns = ['lyrics'])

    test = df_test['lyrics'].values

    pred  = final_clf.predict(test)
    #print(pred)
    return pred







print('EOF...')
