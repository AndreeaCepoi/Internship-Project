#!/bin/bash

input_file="bashcrc.txt"
output_file="bashcrc"

declare -A dictionary

while IFS='=' read -r key value
do
	dictionary["$key"]=$value

done < <(grep '=' "$input_file")


for key in "${!dictionary[@]}"
do
	sed -i "/^[[:space:]]*#/!s/$key=.*$/$key=${dictionary[$key]//\//\\/}/" "$output_file"
        echo "Updated $key"
done
