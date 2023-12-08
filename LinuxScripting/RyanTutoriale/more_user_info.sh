#!/bin/bash

user_name=$1
user_age=$2
user_color=$3

current_date=$(date +"%y-%m-%d")
hostname=$(hostname)

message="Hello, $user_name! You are $user_age years old and you like color $user_color"
message+=" Today is $current_date, and you are running this script on the host $hostname"

echo "$message"
