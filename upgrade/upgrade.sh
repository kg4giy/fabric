#! /bin/bash

FILENAME="pi_hosts.txt"
LINES=$(cat $FILENAME)


for LINE in $LINES
	do
		ssh "$LINE"
		sudo apt update
	done
 