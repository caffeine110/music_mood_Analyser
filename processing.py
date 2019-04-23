#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:57:19 2019

@author: gaurav


"""

##########################################################################################
# importing
import re


##########################################################################################
# Global Variables
negations_dic = {"isn't":"is not", "aren't":"are not", "wasn't":"was not", "weren't":"were not",
                "haven't":"have not","hasn't":"has not","hadn't":"had not","won't":"will not",
                "wouldn't":"would not", "don't":"do not", "doesn't":"does not","didn't":"did not",
                "can't":"can not","couldn't":"could not","shouldn't":"should not","mightn't":"might not",
                "mustn't":"must not"}




def get_from_file():
    
    fileName = 'song_text.txt'
    
    file_obj = open(fileName, 'r')
    
    lines = file_obj.readlines()

    song_text = ''
    
    for line in lines:
        song_text += line
        
    for key in negations_dic:    
        song_text = song_text.replace(key, negations_dic[key])    
    
    song_text = song_text.lower()
    
    song_text = song_text.replace('\n',' ')
    song_text = song_text.replace('  ',' ')
    song_text = song_text.replace('   ',' ')
        
    song_text = re.sub('[^a-zA-z0-9\s]','',song_text)
    
    return song_text





##########################################################################################

def lyrics_processing(lyrics):

    song_text = ''

    for line in lyrics:
        song_text += line
        
    for key in negations_dic:    
        song_text = song_text.replace(key, negations_dic[key])    
    
    song_text = song_text.lower()    

    song_text = song_text.replace('\n',' ')
    song_text = song_text.replace('  ',' ')
    song_text = song_text.replace('   ',' ')
        
    song_text = re.sub('[^a-zA-z0-9\s]','',song_text)    
    #print(song_text)
    
    
    return song_text



