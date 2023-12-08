#!/bin/bash

log_file="log.txt"
output_log="replace_log.txt"
replacement_word="AUTOMATION"

> $output_log

for line_number in {63..69}
do
	word_to_replace=$(awk -v line="$line_number" '{if (NR==line) print $6}' "$log_file")
	
	sed -i "${line_number}s/\b${word_to_replace}\b/$replacement_word/" "$log_file"
	
	replaced_letters=$(echo "$replacement_word" | sed 's/./& /g')
	
	echo "<$word_to_replace> was replaced with the letter: [$replaced_letters]" >> "$output_log"

done

echo "Replacement complete"
