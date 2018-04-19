import json
import pprint

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
        reformist_str =reformist_str + j

for i in principlist_json:
    for j in i:
        principlist_str = principlist_str + j

reformist_text.write(reformist_str.encode('utf-8'))
reformist_text.close()

principlist_text.write(principlist_str.encode('utf-8'))
principlist_text.close()

