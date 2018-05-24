# coding: utf-8

"""
Bot pour jouer aux jeux Twitter en masse

By Bibosso

"""

from twitter_follow_bot import search_tweets

# result_type option
result = search_tweets('RT Follow', count=1, lang='fr')
#print(result)
print('\n')

if 'statuses' in result:

    list_result = result['statuses']
    dataInfo_research = result['search_metadata']
    print('\n')
    print('-- INFO --')
    print('Completed request in : %s' % (dataInfo_research['completed_in']))
    print('Number Result : %s' % (dataInfo_research['count']))
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
        print('==> Posted by : %s' %(elt['user']['screen_name']))
        print('==> Description User : %s' %(elt['user']['description']))
        print('\n')
        print('==> Twitted message : %s' %(elt['text']))











