#!/bin/bash

search_string=$1
shift

for file in $@
do
	if [ ! -f $file ]
	then
		echo Error: File $file not found
		continue
	fi
	
	occurrences=$(grep -c $search_string $file)

	echo Occurrences of $search_string in $file : $occurrences

done

#acepoi@Ubuntu22:~/Internship-Project/LinuxScripting$ ./counter_v2.sh StrictHostKeyChecking bashcrc bashcrc.txt
#Occurrences of StrictHostKeyChecking in bashcrc : 4
#Occurrences of StrictHostKeyChecking in bashcrc.txt : 2

