#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        else:
            return 0

    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit)
        print("{:d}".format(subscribers_count))
