#!/bin/bash
# Sends a GET request with custom header variable
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
