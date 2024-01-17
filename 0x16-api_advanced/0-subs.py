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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0)\
 Gecko/20100101 Firefox/76.0"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    return 0
