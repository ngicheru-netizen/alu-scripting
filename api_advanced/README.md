Learning how to create and modify APIs

## Known Issue: Reddit API Returns `403 Blocked`

### Summary
The `api_advanced` tasks (`0-subs.py`, `1-top_ten.py`, etc.) query the public
Reddit JSON endpoints (e.g. `https://www.reddit.com/r/<subreddit>/about.json`).
When run from my development environment, **every request returns
`HTTP/1.1 403 Blocked`** with an HTML block page instead of JSON, causing
`requests` to raise `JSONDecodeError` or the functions to return `None`/`0`.

This is a **network/edge-level block from Reddit's CDN**, not a bug in the
script logic. The functions are written to the task spec and work correctly
when run from a network Reddit does not block (e.g. the project's automated
checker).

### Evidence
Response received for a valid, existing subreddit:

HTTP/1.1 403 Blocked
Connection: close
Content-Type: text/html
Via: 1.1 varnish
Server: snooserv
...

<body class=theme-beta> ... (HTML block page, not JSON) ... ```
What I tried (all returned 403)
Attempt	Result
Custom User-Agent (Reddit-recommended format)	403
Real browser User-Agent (Chrome on macOS)	403
Full browser headers (Accept, Accept-Language)	403
old.reddit.com host instead of www.reddit.com	403
Mobile hotspot network	403
Home Wi-Fi network	403
allow_redirects=False per task requirement	403
Because the block persists across multiple IPs, User-Agents, headers, and
hosts, the cause is Reddit's bot/TLS fingerprinting or regional edge
blocking — none of which can be resolved from the client code.

### Diagnostic script used - AI Generated (because I was going crazy)

#!/usr/bin/python3
"""Diagnostic: test which request variations Reddit will accept."""
import requests

tests = {
    "1. minimal UA": (
        "https://www.reddit.com/r/programming/about.json",
        {"User-Agent": "myapp/1.0"},
    ),
    "2. browser UA only": (
        "https://www.reddit.com/r/programming/about.json",
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0 Safari/537.36"},
    ),
    "3. full browser headers": (
        "https://www.reddit.com/r/programming/about.json",
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0 Safari/537.36",
         "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9"},
    ),
    "4. old.reddit minimal": (
        "https://old.reddit.com/r/programming/about.json",
        {"User-Agent": "myapp/1.0"},
    ),
    "5. old.reddit browser": (
        "https://old.reddit.com/r/programming/about.json",
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 Chrome/120.0 Safari/537.36"},
    ),
}

for name, (url, headers) in tests.items():
    try:
        r = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        print(name, "->", r.status_code, "|", r.headers.get("Content-Type", "")[:30])
    except Exception as e:
        print(name, "-> ERR", str(e)[:60])
Output (all variations blocked):


1. minimal UA -> 403 | text/html
2. browser UA only -> 403 | text/html
3. full browser headers -> 403 | text/html
4. old.reddit minimal -> 403 | text/html
5. old.reddit browser -> 403 | text/html
Conclusion
The scripts are implemented to specification (custom User-Agent, no redirect
following, correct JSON parsing, 0/None on failure). The 403 Blocked
responses are caused by Reddit-side access restrictions on my environment and
are outside the scope of the code. The functions are expected to pass when
executed from an unblocked network.



