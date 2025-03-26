#!/bin/bash
#Stress-ng calls
#all disabled because this prevented vm from functioning
#stress-ng --class cpu --all 1 --timeout 0
#stress-ng --class memory --all 1 --timeout 0
#stress-ng --class io --all 1 --timeout 0
#stress-ng --class filesystem --all 1 --timeout 0
#stress-ng --class network --all 1 --timeout 0

#Data collection
while true
do
  top -bn 1 | sed -n '3p' > cpupipe &
  top -bn 1 | sed -n '4p' > mempipe &
  #5 second delay for testing
  sleep 5
done
