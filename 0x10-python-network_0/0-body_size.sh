#!/bin/bash
# A script to display the length of a document body fetched from a URL in bytes
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
