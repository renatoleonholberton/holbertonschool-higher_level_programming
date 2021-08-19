#!/bin/bash
# Send a POST request with data as JSON
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
