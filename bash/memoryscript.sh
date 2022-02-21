#!/bin/bash

# This script shows the remaining amount of memory in the system/

# This script uses the awk command to scan the file line by line
# and pull out the data we need.

# We use awk to search the meminfo file on the system and split the lines into 
# fields and search for the line with the words 'MemTotal' in it
# We then print the second field in that line(which is the number we want) and
# set it equal to the MEMORY variable. We then echo this variable with text
# to display the data we need.

MEMORY=$(awk '/MemTotal/ {print $2}' /proc/meminfo)

echo "You have $MEMORY kb of memory remaining"
