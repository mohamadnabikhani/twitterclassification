# -*- coding: utf-8 -*-

import twitter
import json
import local_setting

api = twitter.Api(consumer_key=local_setting.CONSUMER_KEY,
                  consumer_secret=local_setting.CONSUMER_SECRET,
                  access_token_key=local_setting.ACCESS_TOKEN_KEY,
                  access_token_secret=local_setting.ACCESS_TOKEN_SECERT,
                  tweet_mode='extended',
                  )

f = open('data.txt', 'w')

jsonfile = open('jf.json', 'w')

data = []
alltweets = ''


def get_user_timeline(screen_name):
    alltweets = []
    new_tweets = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=False, exclude_replies=False)
    for i in new_tweets:
        alltweets.append(i.full_text)
    oldest = new_tweets[-1].id - 1

    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        new_tweets = api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=False, exclude_replies=False,
                                         max_id=oldest)
        for i in new_tweets:
            alltweets.append(i.full_text)
        print len(new_tweets)
        try:
            oldest = new_tweets[-1].id - 1
        except:
            break
        print "...%s tweets downloaded so far" % (len(alltweets))

    # json.dump(alltweets, outfile)
    # outfile.close()
    return alltweets



def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z



def make_json_file(data, file):
    json.dump(data, file)
    file.close()


def create_main_tweets(data):
    alltweets = []
    for i in data:
        try:
            new_tweets = get_user_timeline(i)
            alltweets.append(new_tweets)
            print "####"
            print len(new_tweets)
        except Exception as e:
            print(e)
    return alltweets

if __name__ == '__main__':

    reformist = ['mah_sadeghi', 'abdollahram', 'eshaq_jahangiri' ,'AMasjedjamei', 'mostafatajzade' ,'khatami_ir',
                 'ebtekarm_ir', 'mowlaverdi', 'kavakebian_ir', '']
    principlist = ['smmirsalim', 'raisi_org', 'DrSaeedjalili', 'HaddadAdel_ir', 'ir_rezaee', 'TavakoliDr',
                   'Zarghami_ez', 'Dastjerdi_ir', 'zakani_ir', 'dr_naghavy', 'drmkhazali' ]

    reformist_tweets = create_main_tweets(reformist)
    principlist_tweets = create_main_tweets(principlist)


    reformist_file = open('reformist.json', 'w')
    principlist_file = open('principlist.json', 'w')

    make_json_file(reformist_tweets, reformist_file)
    make_json_file(principlist_tweets, principlist_file)




