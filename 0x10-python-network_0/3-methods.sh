#!/bin/bash
# Sends a DELETE request to a URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
