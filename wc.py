#!/usr/bin/env python

from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud

from os import path
from PIL import Image
import numpy as np
# from clean_data import remove_unknownchar
import re

def remove_unknownchar(text):
    a = "\xe2\x81\xa9"
    a1 = "\xe2\x81\xa9 "
    a2 = " \xe2\x81\xa9"
    a3 = " \xe2\x81\xa9 "
    b = "\xe2\x81\xa7"
    b1 = " \xe2\x81\xa7"
    b2 = "\xe2\x81\xa7 "
    b3 = " \xe2\x81\xa7 "
    c = re.sub(r'[{0}{1}{2}{3}{4}{5}{6}{7}]'.format(a,a1,a2,a3,b,b1,b2,b3), ' ', text)
    return c


d = path.dirname(__file__)
text = open(path.join(d, 'renew_reformist.txt'),encoding='utf-8').read()

twitter_mask = np.array(Image.open(path.join(d, "logo.png")))



STOPWORD = set([i for i in open((path.join(d, 'stopword.txt'))).read().split('\n')])
# print (type(STOPWORDS))
# print (type(STOPWORD))
STOPWORDS.union(STOPWORD)
stopwords = set(STOPWORDS)

wordcloud = PersianWordCloud(
    only_persian=False,
    max_words=200,
    stopwords=stopwords,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    random_state=True,
    background_color="white",
    mask=twitter_mask
).generate(remove_unknownchar(text))

image = wordcloud.to_image()
image.show()
image.save('reformist_mask.png')
