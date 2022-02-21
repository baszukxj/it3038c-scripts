#!/bin/bash

MEMORY=$(awk '/MemTotal/ {print $2}' /proc/meminfo)

echo "You have $MEMORY kb of memory remaining"
