#!/bin/bash

if [ ! -e $1 ]; then
    echo File does not exist: $1
    exit 1
fi

if [ -x $1 ]; then
    echo The file $1 is executable
else
    echo The file $1 is not executable
fi

if [ -w $1 ]; then
    echo The file $1 is writable
else
    echo The file $1 is not writable
fi
