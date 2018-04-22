# -*- coding: utf-8 -*-

import re
from hazm import *

normalizer = Normalizer()

def remove_url(text):
    new_text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
    return new_text

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

def reformat_hashtag(text):
    if '#' in text:
        text = text.replace('#', ' ').replace('_', ' ')
    return text

def reformat_numberinchars(text):
    if not text.isdigit():
        text = ''.join([i for i in text if not i.isdigit()])
    return text

def remove_english_char(text):
    a = re.sub(r'[a-zA-Z]', '', text)
    return a


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def remove_space(text):
    if len(text) > 2:
        if text[0] == ' ':
            text = text[1:-1]

        if text[-1] == ' ':
            text = text[0:-2]
    return text

def remove_underline(text):
    a = re.sub(r'[_]', ' ', text)
    return a

def reformat_mi(text):
    return text.replace("می‌", "می ")


def reformat_ha(text):
    return text.replace("‌ها", " ها")

def reformat_mention(text):
    if '@' in text:
        text = text.replace(text, ' ')
    return text



def tokenize(text):
    text = remove_unknownchar(text)
    text = normalizer.normalize(text)
    words = word_tokenize(text)
    tokenize_words = []

    for i in words:
        if not isEnglish(i):

            i = reformat_mention(i)
            tokenize_words.append(remove_unknownchar(remove_underline(
                reformat_numberinchars(
                    remove_english_char(remove_space(
                        reformat_hashtag(i)
                    )
                    )
                )
            )

            ))
    count = 0
    for i in tokenize_words:
        if (u"\xe2\x81\xa9" in i ) or (u"\xe2\x81\xa7" in i):
            count = count +1
    # print "######"
    # print count
    return tokenize_words

