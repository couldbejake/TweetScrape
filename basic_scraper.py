# run via cron every 15 minutes

import os
import time
import json
import requests
import random
import pickle
import subprocess

def dump_json(obj):
    with open('data.json', 'w') as outfile:
        json.dump(obj, outfile)

def generate_token():
    user_agent = f'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
    guest_token = subprocess.check_output("curl -skL https://twitter.com/ -H {user_agents[1]} --compressed | grep -o 'gt=[0-9]*' | sed s.gt=..", shell=True, text=True).strip()
    return guest_token

def twitter_data(search_term, since, until):
    
    url = 'https://api.twitter.com/2/search/adaptive.json'

    params = {
        'include_profile_interstitial_type': 1,
        'include_blocking': 1,
        'include_blocked_by': 1,
        'include_followed_by': 1,
        'include_want_retweets': 1,
        'include_mute_edge': 1,
        'include_can_dm': 1,
        'include_can_media_tag': 1,
        'skip_status': 1,
        'cards_platform':'Web-12',
        'include_cards': 1,
        'include_ext_alt_text':'true',
        'include_quote_count':'true',
        'include_reply_count': 1,
        'tweet_mode':'extended',
        'include_entities':'true',
        'include_user_entities':'true',
        'include_ext_media_color':'true',
        'include_ext_media_availability':'true',
        'send_error_codes':'true',
        'simple_quoted_tweet':'true',
        'q': str(search_term) + " since:" + str(since) + " until:" + str(until),
        'count':'50',
        'query_source':'typed_query',
        'pc': 1,
        'spelling_corrections': 'false',
        'ext':'mediaStats%2ChighlightedLabel',
    }

    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': generate_token()
    }

    res = requests.get(url, params=params, headers=headers)

    json_data = res.json()


    tw_count = len(json_data['globalObjects']['tweets'])

    print(str(tw_count) + " tweets collected.")


twitter_data("$fb", '2015-01-01', '2015-01-06')
