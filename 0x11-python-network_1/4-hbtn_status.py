#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    body = r.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
