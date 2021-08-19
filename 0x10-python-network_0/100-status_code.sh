#!/bin/bash
# Displays the status code of an http response
curl -s -o /dev/null -w "%{http_code}" "$1"
