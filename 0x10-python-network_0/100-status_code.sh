#!/bin/bash
# Script for displaying status code of server
curl -L -s -X HEAD -w "%{http_code}" "$1"
