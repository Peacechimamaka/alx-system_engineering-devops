#!/usr/bin/python3
"""
A function queries Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a subreddit given.
    """
    
    uri_a = '{base}/r/{subreddit}/about.json'.format(base=base_url,
                                                       subreddit=subreddit)
    url_b = 'https://www.reddit.com'

    # Set an User-Agent
    agent = {'User-Agent': 'Python/requests'}

    # Get the Response of the Reddit API
    response = requests.get(uri_a, headers=agent,
                       allow_redirects=False)

    # If the subreddit is invalid
    if response.status_code in [302, 404]:
        return 0

    # Returning the total subscribers of the subreddit
    return response.json().get('data').get('subscribers')
