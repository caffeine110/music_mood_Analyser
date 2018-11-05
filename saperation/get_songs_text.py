#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 03:26:12 2018

@author: gaurav

AIM : to saperate only songs
        saperation file


    input file : formated/songdata.csv
    output file : seperation/only_songs.csv

"""



import pandas as pd

filePath = 'formated/songdata.csv'
df = pd.read_csv(filePath, usecols=['text'])


new_filePath = 'saperation/only_songs.csv'
df.to_csv(new_filePath, index=False)
