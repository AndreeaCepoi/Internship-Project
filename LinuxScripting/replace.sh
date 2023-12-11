#!/bin/bash

log_file="log.txt"
output_log="replace_log.txt"
replacement_word="AUTOMATION"

> $output_log

replaced_letters=($(echo "$replacement_word" | sed 's/./& /g'))

for line_number in {63..72}
do
        
        word_to_replace=$(awk -v line="$line_number" '{if (NR==line) print $6}' "$log_file")
        
	sed -i "${line_number}s/\b${word_to_replace}\b/${replaced_letters[0]}/" "$log_file"
	
	echo "<$word_to_replace> was replaced with the letter: $replaced_letters" >> "$output_log"
	
	replaced_letters=("${replaced_letters[@]:1}")
   	
done

echo "Replacement complete"
