#!/bin/bash

read -p 'Enter your name: ' user_name
read -p 'Enter your age: ' user_age
read -p 'Enter a color: ' user_color

message="Hello, $user_name! You are $user_age years old and you like color $user_color"

echo "$message"
