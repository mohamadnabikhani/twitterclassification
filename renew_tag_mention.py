# -*- coding: utf-8 -*-
import clean_data

reformist_text = open('reformist.txt', 'r').read().decode('utf-8')
principlist_text = open('principlist.txt', 'r').read().decode('utf-8')



reformist_str = []
principlist_str = []


reformist_arr = clean_data.tokenize(reformist_text)
principlist_arr = clean_data.tokenize(principlist_text)

print len(reformist_arr)

new_reformist_text = clean_data.remove_unknownchar(' '.join(reformist_arr))
new_principlist_text = ' '.join(principlist_arr)

print len(new_reformist_text)

reformist_renew = open('renew_reformist.txt', 'w')
principlist_renew = open('renew_principlist.txt', 'w')

reformist_renew.write(new_reformist_text.encode('utf-8'))
reformist_renew.close()


principlist_renew.write(new_principlist_text.encode('utf-8'))
principlist_renew.close()