#!/bin/bash

lower_limit=$1
upper_limit=$2
random_nr=$((lower_limit + RANDOM % (upper_limit - lower_limit +1)))

echo "Random Nr between $lower_limit and $upper_limit: $random_nr"
