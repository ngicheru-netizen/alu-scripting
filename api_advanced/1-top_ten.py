#!/usr/bin/python3
"""Find top 10 hot posts of subreddit from reddit API"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "macos:com.intranet.apistuff:v1.0.0(by /u/PlasticDrummer2706)"
    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        parsed_data = response.json()
        hot_posts = parsed_data["data"]["children"]

        for post in hot_posts[:10]:

            print(post["data"]["title"])
        else:
            print(None)


if __name__ == "__main__":
    top_ten("programming")
