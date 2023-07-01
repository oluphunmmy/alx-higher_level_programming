#!/usr/bin/python3
"""
Use requests package to make a post request sending email param
and display body of response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    req = requests.post(url, data=payload)
    print(req.text)
