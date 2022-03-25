#!/bin/sh

#doppler secrets download --no-file --format env-no-quotes >| docker/local/vars.env

while read -r line; do
    echo $line | grep . | grep -v '^#' && export $line
done < docker/local/vars.env
