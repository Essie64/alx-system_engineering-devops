#!/usr/bin/python3
"""
query Reddit API and print titles of the first 10 hot posts for a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function to print titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': }
    params = {'limit': 10}'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            if not posts:
                print("No posts found.")
            else:
                for post in posts:
                    title = post.get('data', {}).get('title')
                    print(title)

        else:
            print(f"Error: {response.status_code}")
            print("None")

    except Exception as e:
        print(f"Error: {e}")
        print("None")
