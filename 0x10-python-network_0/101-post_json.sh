#!/bin/bash
# Script to post json data files and to test a server
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
