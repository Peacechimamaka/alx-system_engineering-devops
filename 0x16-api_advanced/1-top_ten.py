#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first 10"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for
    a given subreddit.
    """
    url_given = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers_given = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params_given = {
        "limit": 10
    }
    res = requests.get(url_given, headers=headers_given, params=params_given,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    output = res.json().get("data")
    [print(c.get("data").get("title")) for c in output.get("children")]
