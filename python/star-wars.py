#!/usr/bin/python3
import requests
import json

auth_token='sdfghjkloerdtfyguhiopfghjkl;fghjkl'
headers = {'Authorization': 'Bearer ' + auth_token}
data = {'app' : 'aaaaa'}

next = 'https://swapi.dev/api/people'

print('People...')

while next and len(next) > 0:
    response = requests.get(next, headers=headers)
    print('ok={} status={}'.format(response.ok, response.status_code))
    data = json.loads(response.text)
    next = data['next']
    print('results={} next={}'.format(len(data['results']), next))

print('People...Finished')
