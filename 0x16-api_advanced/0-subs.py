#!/usr/bin/python3
'''Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
'''
from requests import get


def number_of_subscribers(subreddit):
    '''
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    Returns: 0 if an invalid subreddit is given
    '''

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
