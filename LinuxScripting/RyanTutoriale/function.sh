#!/bin/bash

print_som () {
	echo Hello  $1
	return 5
}

print_som Mars
print_som Pluto
echo The return value of $?
