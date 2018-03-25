# -*- coding: utf-8 -*-

import twitter
import json
proxies = {
    'http': 'http://127.0.0.1:8118',
    'https': 'http://127.0.0.1:8118',
}

api = twitter.Api(consumer_key='JFNvl01Y54C4rXrMhd33RHjVT',
                  consumer_secret= 'ViHdf1wgVjeRUqlHgTfgxZ5mfPnEcRLtl0qyGyenz8VCJVCEdN',
                  access_token_key='2303600917-J34dNVYpIFmabWBNVYIXI9JT915hFY0usNNw8oK',
                  access_token_secret='EluJqeWi8pvTVRn49s8R5OT0MMxc3Wi7zoOIrRX0AZ7jz',
                  tweet_mode= 'extended',
				  )

f=open('data.txt', 'w')
outfile = open('data.json', 'w')
jsonfile = open('jf.json','w')


data = []
alltweets = ''
def get_all_tweets(search):
	global alltweets
	finaldata = {}
	# b = api.GetSearch(term=search, return_json=True,count=100,lang='fa',until='2018-03-16',since='2018-03-15')

	for i in range(7):
		b = api.GetSearch(term=search, return_json=True, count=100, lang='fa', until='2018-03-{0}T06:00:00'.format(16+i), since='2018-03-{0}T22:00:00'.format(15+i)
						  )
		compute(b)
		finaldata.update(b)

	# print b

	# statuses = b['statuses']
	# print len(statuses)
	# for status in statuses:
	# 	s={}
	# 	if status.has_key('full_text'):
	# 		alltweets += status['full_text']
	# 		s['text'] = status['full_text']
	# 	alltweets +='\n'
    #
	# 	s['date'] = status['created_at']
	# 	data.append(s)
	json.dump(finaldata,jsonfile)
	jsonfile.close()

	f.write(alltweets.encode('utf-8'))
	f.close()

	json.dump(data, outfile)
	outfile.close()

def merge_two_dicts(x,y):
	z = x.copy()
	z.update(y)
	return z


def compute(b):
	global alltweets
	statuses = b['statuses']
	print len(statuses)
	for status in statuses:
		s = {}
		if status.has_key('full_text'):
			alltweets += status['full_text']
			s['text'] = status['full_text']
		alltweets += '\n'

		s['date'] = status['created_at']
		data.append(s)



if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("ترامپ".decode('utf-8'))

