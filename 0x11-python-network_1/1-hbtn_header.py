#!/usr/bin/python3
"""Script that will take a URL,then send request
to URL and display value of the X-Request-Id
variable that found in header of the response."""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
