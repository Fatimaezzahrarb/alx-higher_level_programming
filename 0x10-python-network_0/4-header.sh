#!/bin/bash
# script used to send custom headers to the servers
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
