#!/usr/bin/python3
"""Recursive function to Find top 10 hot posts of subreddit from reddit API"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "macos:com.intranet.apistuff:v1.0.0(by /u/PlasticDrummer2706)"
    headers = {"User-Agent": user_agent}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Error: Received status code {}".format(response.status_code))
        return hot_list

    try:

        data = response.json()
    except ValueError:
        print("Not correct JSON")
        return hot_list

    if "data" not in data or "children" not in data["data"]:
        return hot_list

    children = data["data"]["children"]

    hot_list.extend(children)

    # base case

    next_after = data["data"].get("after")

    if next_after is None:
        return hot_list

    # recursive case
    return recurse(subreddit, hot_list, after=next_after)


if __name__ == "__main__":
    subreddit = "programming"
    hot_posts = recurse(subreddit)
