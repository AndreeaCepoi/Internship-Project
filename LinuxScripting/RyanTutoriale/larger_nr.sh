#!/bin/bash

if [ $1 -gt $2 ]
then
	echo The larger number is $1
elif [ $1 -lt $2 ]
then
	echo The larger number is $2
else
	echo The numbers are equal
fi
