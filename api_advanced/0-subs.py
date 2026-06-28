#!/usr/bin/python3
"""Find total subscriber count of subreddit
from reddit API"""

import requests


def number_of_subscribers(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "macos:com.intranet.apistuff:v1.0.0(by /u/PlasticDrummer2706)"
    headers = {"User-Agent": user_agent}

    response_object = requests.get(url, headers=headers, allow_redirects=False)

    if response_object.status_code == 200:
        parsed_data = response_object.json()
        total_subscribers = parsed_data["data"]["subscribers"]

        return total_subscribers
    else:
        return 0


print(number_of_subscribers("programming"))
