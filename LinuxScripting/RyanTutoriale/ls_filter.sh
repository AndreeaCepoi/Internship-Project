#!/bin/bash

ls -l | awk '{print "File: " $9, "Size: " $5, "Owner: " $3}'

