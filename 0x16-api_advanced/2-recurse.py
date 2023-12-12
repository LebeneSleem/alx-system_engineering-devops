#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and returning
titles of all hot articles for a given subreddit.
"""

import requests
after = None


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API and return titles of
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store titles of hot articles.
        after (str): Parameter used for pagination to get the
        next set of results.

    Returns:
        list or None: List containing titles of hot articles or
        None if no results are found.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
