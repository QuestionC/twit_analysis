# Pull the data from twitter.  Analyze it offline cuz of API limits


import TwitterAPI
import json
import itertools
import time

import secrets

screen_name = 'iamcardib'
api = TwitterAPI.TwitterAPI(secrets.consumer_key, secrets.consumer_secret, secrets.access_token, secrets.access_token_secret, auth_type='oAuth2')

root_tweet = 'url:twitter.com/realDonaldTrump/status/1115295440558280704'

next_param = None
# next_param = "eyJhdXRoZW50aWNpdHkiOiJlNDZmMTJjZWViNWFhZDEyMzk5YWYyMzhiNzU1Yjc3NWU4Zjg2NmZkMzBlMTMyYTIwMWIwMzdjOTQwMmY0MDQ3IiwiZnJvbURhdGUiOiIyMDE5MDMwOTAwMDAiLCJ0b0RhdGUiOiIyMDE5MDQwODIxNDkiLCJuZXh0IjoiMjAxOTA0MDgyMTQ5MDAtMTExNTMwNjY5NzY2NzU2NzYxOC0wIn0="

for i in itertools.count(30):
    print ('Doing request with next_param = {}'.format(next_param))
    r = api.request('tweets/search/30day/:dev', {'query':root_tweet, 'next': next_param})
    j = json.loads(r.text)

    with open('twit' + str(i) + '.json', 'w') as fp:
        json.dump(j, fp, indent=2)
    
    if 'next' not in j:
        break
    next_param = j['next']
    time.sleep(3) # Twitter rate limiting



