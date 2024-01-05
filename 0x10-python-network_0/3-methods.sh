#!/bin/bash
# Display the HTTP method that the server will accept
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
