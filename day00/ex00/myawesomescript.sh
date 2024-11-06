#!/bin/sh

# grep -o 'href="[^"]*' finds the part of the HTML containing href="URL" and captures everything up to the next "

curl -s $1 | grep -o 'href="[^"]*' | cut -d '"' -f2