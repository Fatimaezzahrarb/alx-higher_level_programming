#!/usr/bin/python3
"""Python script for posting the data to web servers."""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.post(argv[1], data={'email': argv[2]}).text)
