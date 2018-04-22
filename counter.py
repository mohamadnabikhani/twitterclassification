# -*- coding: utf-8 -*-
from hazm import *

reformist_text = open('renew_reformist.txt', 'r').read().decode('utf-8')
principlist_text = open('renew_principlist.txt', 'r').read().decode('utf-8')

reformist_arr = word_tokenize(reformist_text)
principlist_arr = word_tokenize(principlist_text)

reformist_counter = {}
reformist_number = 0
for i in reformist_arr:
    reformist_number += 1
    if i not in reformist_counter.keys():
        reformist_counter[i] = 1
    else:
        reformist_counter[i] = reformist_counter[i] + 1


principlist_counter = {}
principlist_number = 0
for i in principlist_arr:
    principlist_number += 1
    if i not in principlist_counter.keys():
        principlist_counter[i] = 1
    else:
        principlist_counter[i] += 1

reformist_nrom = {}
for key in reformist_counter.keys():
    reformist_nrom[key] = (reformist_counter[key] * 1.0) / reformist_number

principlist_norm = {}
for key in principlist_counter.keys():
    principlist_norm[key] = (principlist_counter[key] * 1.0) / principlist_number


compare = {}
for key in reformist_nrom.keys():
    if key in principlist_norm.keys():
        compare[key] = reformist_nrom[key] - principlist_norm[key]

import csv

compare2 = {}
for key in compare.keys():
    compare2[key.encode('utf-8')] = compare[key]



with open('compare.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, compare2.keys())
    w.writeheader()
    w.writerow(compare2)
