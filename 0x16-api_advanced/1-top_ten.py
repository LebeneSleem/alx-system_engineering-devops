#!/usr/bin/python3
"""
Module for interacting with the Reddit API and printing titles of
the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Reddit API endpoint for hot posts in the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_app/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are posts in the response
        if 'data' in data and 'children' in data['data']:
            # Print titles of the first 10 posts
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
        else:
            print("No posts found for the subreddit.")
    elif response.status_code == 404:
        # Subreddit not found, print None
        print(f"Subreddit '{subreddit}' not found.")
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    top_ten(subreddit_name)
