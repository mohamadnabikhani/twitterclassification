#!/usr/bin/env python

from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud

from os import path
from PIL import Image
import numpy as np

d = path.dirname(__file__)
text = open(path.join(d, 'data.txt'),encoding='utf-8').read()

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
).generate(text)

image = wordcloud.to_image()
image.show()
image.save('twitter_mask.png')
