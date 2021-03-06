import os
import time
import json
import requests
import random
import subprocess
import time

def dump_json(obj):
    with open('data.json', 'w') as outfile:
        json.dump(obj, outfile)


def get_twitter_gt():
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }

    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
    guest_token = (response.json()['guest_token'])

    return guest_token;

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
        'cards_platform': 'Web-12',
        'include_cards': 1,
        'include_ext_alt_text': 'true',
        'include_quote_count': 'true',
        'include_reply_count': 1,
        'tweet_mode': 'extended',
        'include_entities': 'true',
        'include_user_entities': 'true',
        'include_ext_media_color': 'true',
        'include_ext_media_availability': 'true',
        'send_error_codes': 'true',
        'simple_quoted_tweet': 'true',
        'q': str(search_term) + " since:" + str(since) + " until:" + str(until),
        'count': '50',
        'query_source': 'typed_query',
        'pc': 1,
        'spelling_corrections': 'false',
        'ext': 'mediaStats%2ChighlightedLabel',
    }

    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-guest-token': get_twitter_gt()
    }

    res = requests.get(url, params=params, headers=headers)

    json_data = res.json()

    tweets = json_data['globalObjects']['tweets']

    tweets_out = []
    
    for tweet_id in tweets:
        full_text = json_data['globalObjects']['tweets'][tweet_id]['full_text']
        safe_text = full_text.encode("ascii", errors="ignore").decode()
        tweets_out.append(safe_text)

    return tweets_out

tweets = twitter_data("$fb", '2015-01-01', '2015-01-06')

print(str(len(tweets)) + " tweets collected!")

for tweet in tweets:
    print(tweet + '\n')





