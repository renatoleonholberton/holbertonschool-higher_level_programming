#!/bin/bash
# Displays an http response body size
curl -s "$1" | wc -c
