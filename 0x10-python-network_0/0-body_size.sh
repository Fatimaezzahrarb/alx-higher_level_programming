#!/bin/bash
# script to get to body size of the request
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
