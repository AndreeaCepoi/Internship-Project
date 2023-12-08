#!/bin/bash

for value in {1..10}
do
	if (( $value % 2 == 0 ))
	then
		echo $value is even
	else
		echo $value is odd
	fi
done
