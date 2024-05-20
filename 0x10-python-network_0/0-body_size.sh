#!/usr/bin/env bash
# A script to display the length of a http document body in bytes
# Usage: ./0-body_size.sh URL

if [ "$#" -ge 1 ]
then
	curl -sI "$1" | grep Content-Length | cut -d " " -f 2
fi
