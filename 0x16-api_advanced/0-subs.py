#!/usr/bin/python3
"""
Module for interacting with the Reddit API and retrieving the
number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        If the subreddit is invalid, return 0.
    """
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_app/1.0'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and return the number of subscribers
        return data['data']['subscribers']
    elif response.status_code == 404:
        # Subreddit not found, return 0
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        # Handle other errors
        print(f"Error: {response.status_code}")
        return 0


if __name__ == "__main__":
    # Example usage:
    subreddit_name = 'python'
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers in r/{subreddit_name} is: {subscribers}")
