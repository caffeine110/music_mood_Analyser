import re
from textblob import TextBlob


song1 = "She's just my kind of girl, she makes me feel fine Who could ever believe that she could be mine?  She's just my kind of girl, without her I'm blue  And if she ever leaves me what could I do, what could I do?"

song2 = "And when we go for a walk in the park  And she holds me and squeezes my hand  We'll go on walking for hours and talking  About all the things that we plan "

song3 = "She's just my kind of girl, she makes me feel fine  Who could ever believe that she could be mine?  She's just my kind of girl, without her I'm blue  And if she ever leaves me what could I do, what could I do?"

song4 = "fuck you"

song5 = "thes is very bad or even wotst"




song_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", df).split())
so = ''

for i in song_n:
    so = so + ' ' + i 


print(so)

analysis = TextBlob(so)

if analysis.sentiment.polarity > 0:
    print('positive')
elif analysis.sentiment.polarity == 0:
    print('neutral')
else:
    print('negative')





########################################################################
#import pandas
import csv

filepath = 'd.csv'

with open('d.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        song_text = row['text']
        
        song_n = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", song_text).split())
        so = ''

        for i in song_n:
            so = so + ' ' + i 

        
        print(so)
        
        analysis = TextBlob(so)
        
        if analysis.sentiment.polarity > 0:
            print('positive')
        elif analysis.sentiment.polarity == 0:
            print('neutral')
        else:
            print('negative')
