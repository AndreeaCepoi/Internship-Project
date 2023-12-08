#!/bin/bash

search_string=$1
filename=$2

if [ ! -f $filename ]
then
	echo Error: File $filename not found
	exit 1
fi

occurrences=$(grep -c $search_string $filename)

echo Occurrences of $search_string in $filename : $occurrences



#acepoi@Ubuntu22:~/Internship-Project/LinuxScripting$ ./counter.sh StrictHostKeyChecking bashcrc
#Occurrences of StrictHostKeyChecking in bashcrc : 4


