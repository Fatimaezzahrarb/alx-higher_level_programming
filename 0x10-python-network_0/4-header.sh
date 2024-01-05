#!/bin/bash
# script used to send custom headers to the servers
curl -s "$1" -H "X-School-User-Id: 98"
