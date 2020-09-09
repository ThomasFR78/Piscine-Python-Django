#!/bin/bash
# myawesomescript.sh


#curl $1 -si | grep -oP ':\/\/(.*)"'
curl $1 -si | grep -oP 'Location: (.*)' | cut -c 11-


#:\/\/(.*)"

#'www.(.*)\/"'