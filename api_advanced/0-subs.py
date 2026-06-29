#!/usr/bin/python3
"""Query the Reddit API over HTTP and return a subreddit's subscriber count.

Sends an HTTP GET request to the Reddit API endpoint for a given subreddit,
parses the JSON response, and returns the total number of subscribers.
Returns 0 for an invalid subreddit (non-200 response / redirect).
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit, or 0 if invalid."""

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


if __name__ == "__main__":
    print(number_of_subscribers("programming"))
