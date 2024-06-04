#!/usr/bin/python3
"""Count it - a recursive function that queries Reddit API"""
import requests
import sys
import re


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title_r = hot_posts[0]['data']['title'].split()
    for word in title_r:
        for key in dictionary.keys():
            cc = re.compile("^{}$".format(key), re.I)
            if cc.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries to Reddit API """
    agent = 'Mozilla/5.0'
    header = {
        'User-Agent': agent
    }

    paramets = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                       headers=header,
                       params=paramets,
                       allow_redirects=False)

    if response.status_code != 200:
        return None

    dic = response.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for item in l:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
