# coding: utf-8

"""
Bot pour jouer aux jeux Twitter en masse

By Bibosso

"""

from twitter_follow_bot import search_tweets


tag = 'macron'

result = search_tweets(tag, count=1, lang='fr', result_type='mixed')
#print(result)


if 'statuses' in result:

    list_result = result['statuses']
    dataInfo_research = result['search_metadata']
    print('\n')
    print('-- INFO --')
    print('Completed request in : %s' % (dataInfo_research['completed_in']))
    print('Number max Result required : %s' % (dataInfo_research['count']))
    print('Query : %s' % (dataInfo_research['query']))
    print('\n')


    for elt in list_result:

        #for key, value in elt.items():
            #print(key)

        # work return 'entities' key
        # key 'user_mentions' type list()
        # key 'hashtags' type list()

        ent = elt['entities']
        print('==> ' + str(len(ent['user_mentions'])) + ' user mentionned by @')
        countEnt = 1
        for um in ent['user_mentions']:
            print('User mentions ' + str(countEnt) +' : @' + um['screen_name'])
            countEnt += 1

        print('\n')

        print('==> ' + str(len(ent['hashtags'])) + ' hashtags detected by #')
        for h in ent['hashtags']:
            #print(type(h), h)
            print('Hastags detected : #' + h['text'])

        print('\n')

        # url source
        #print('==> Source : %s' %(elt['source']))

        # url search
        if len(ent['urls']) == 0:
            print('==> any link detected')
        else:
            countUrl = 1
            print('==> %s URL detected' %(str(len(ent['urls']))))
            for u in ent['urls']:
                print('==> URL %s : %s'%(str(countUrl), u['expanded_url']))
                countUrl += 1


        print('\n')

        # working return 'metadata' key
        # key 'result_type' type str() exemple : "popular / recent / mixed "
        print('==> Type result : %s' %(elt['metadata']['result_type']))
        print('\n')

        # working return 'user' key  have post
        # key 'id_str'
        # key 'name'
        # key 'screen_name'
        # key 'description'
        # key 'verified' type bool()
        print('==> Posted by scree-name : %s' %(elt['user']['screen_name']))
        print('==> Posted by name : %s' %(elt['user']['name']))
        print('==> Description User : %s' %(elt['user']['description']))
        print('\n')

        print('==> message posted at : %s' %(elt['created_at']))

        # if tweet or retweet
        if elt['text'][:2] == 'RT':
            print('==> detected message is a Retweet')
        else:
            print('==> detected message is a Tweet')

        print('\n')
        print('==> Twitted message : %s' %(elt['text']))


print('\n')











