#!/bin/bash
# script with fun effort for breaking to http protocols on holberton servers
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
