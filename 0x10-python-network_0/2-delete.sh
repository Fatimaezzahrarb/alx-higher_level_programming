#!/bin/bash
# script that will send the DELETE request to the URL as first argument then displays the body of response
curl -s -X DELETE "$1"
