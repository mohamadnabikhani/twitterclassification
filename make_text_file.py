# -*- coding: utf-8 -*-

import json
import pprint
import clean_data
import emojies
import re

reformist = open('reformist.json', 'r')
principlist = open('principlist.json', 'r')

reformist_json = json.load(reformist)
principlist_json = json.load(principlist)
print type(reformist_json)

reformist_text = open('reformist.txt', 'w')
principlist_text = open('principlist.txt', 'w')

reformist_str = ''
principlist_str = ''

for i in reformist_json:
    for j in i:
        new_format = clean_data.remove_url(j)
        reformist_str = reformist_str + new_format + '\n'


for i in principlist_json:
    for j in i:
        new_format = clean_data.remove_url(j)
        principlist_str = principlist_str + new_format + '\n'

principlist_str = re.sub(emojies.emojies_re, "", principlist_str)
reformist_str = re.sub(emojies.emojies_re, "", reformist_str)

reformist_text.write(reformist_str.encode('utf-8'))
reformist_text.close()

principlist_text.write(principlist_str.encode('utf-8'))
principlist_text.close()

