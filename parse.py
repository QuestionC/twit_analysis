import json

with open('out.json') as fp:
    myjson = json.load(fp)

for result in myjson['results']:
    if 'retweeted_status' in result:
        continue
    print('-----')
    if 'extended_tweet' in result:
        print(result['extended_tweet']['full_text'])
    else:
        print(result['text'])

