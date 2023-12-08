#!/bin/bash

while IFS= read -r line
do
   
    variable=$(echo "$line" | cut -d'=' -f1)
    value=$(echo "$line" | cut -d'=' -f2-)

   
    if grep -q "^$variable=" "/home/acepoi/Internship-Project/LinuxScripting/bashcrc"
    then
    
        sed -i "s#^$variable=.*#$variable=$value#" "/home/acepoi/Internship-Project/LinuxScripting/bashcrc"
    
    fi
done < "/home/acepoi/Internship-Project/LinuxScripting/bashcrc.txt"

echo "Search and replace completed successfully."
