# encoding=utf8  
import sys  

from textblob import TextBlob
from textblob.translate import Translator

reload(sys)  
sys.setdefaultencoding('utf8')


T = Translator()


def to_eng(string):
    decoded = T.detect(string.decode('utf-8'))
    if decoded != 'en':
        return T.translate(string.decode('utf-8'), from_lang=decoded, to_lang='en')
    else:
        return string
        

def analyze(string):
    analysis = TextBlob(to_eng(string))
    return analysis.sentiment.polarity*100

