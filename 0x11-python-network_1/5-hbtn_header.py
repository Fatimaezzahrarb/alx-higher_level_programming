#!/usr/bin/python3
"""Python script to test status of web pages."""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
