#!/usr/bin/python3
"""Queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given.
    """
    # Set the Default URL
    url_b = 'https://www.reddit.com'
    uri_a = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set the Query Strings to Request
    payload_va = {'after': after, 'limit': '100'}

    # Get the Response of the Reddit API
    response = requests.get(uri_a, headers=user_agent,
                       params=payload_va, allow_redirects=False)

    # Checks if the subreddit is invalid
    if response.status_code == 200:
        response = response.json()
        hot_posts = response.get('data').get('children')
        after = response.get('data').get('after')

        # Print each hot post title
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Get the next page of hot posts
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
