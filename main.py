'''
TBA
'''

# -*- coding: utf-8 -*-

# from textblob import TextBlob
from textblob.translate import Translator

T = Translator()

with open("list.txt", "r") as lst:
    TBA = []
    for line in lst:
        decoded = T.detect(line.decode('utf-8'))
        if decoded != "en":
            TBA.append(T.translate(line.decode('utf-8'), from_lang=decoded, to_lang='en'))
        else:
            TBA.append(line)


for line in TBA:
    print line
