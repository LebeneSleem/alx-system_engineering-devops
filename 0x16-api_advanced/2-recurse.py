#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and returning
titles of all hot articles for a given subreddit.
"""

import requests


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
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint for hot posts in the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_app/1.0'}

    # Include 'after' parameter if it is provided
    params = {'after': after} if after else {}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are posts in the response
        if 'data' in data and 'children' in data['data']:
            # Append titles to the hot_list
            hot_list.extend([post['data']['title'] for post in data['data']['children']])

            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function with the 'after' parameter
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the hot_list
                return hot_list
        else:
            # No posts found for the subreddit, return None
            return None
    elif response.status_code == 404:
        # Subreddit not found, return None
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    hot_articles = recurse(subreddit_name)

    if hot_articles:
        print(f"Titles of hot articles in r/{subreddit_name}:\n")
        for title in hot_articles:
            print(title)
    else:
        print("No results found for the subreddit.")
