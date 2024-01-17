#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return titles of all hot articles for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to query the Reddit API and return titles of all hot articles for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.
        after (str): Parameter for pagination to get the next set of results.

    Returns:
        list or None: List containing titles or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            if not posts:
                return hot_list

            for post in posts:
                title = post.get('data', {}).get('title')
                hot_list.append(title)

            return recurse(subreddit, hot_list, after)

        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
