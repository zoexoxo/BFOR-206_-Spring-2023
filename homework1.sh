#!/bin/bash

# Input validation
if [[ -z "$1" ]];then
	echo "please provide an input"
	exit 1

#Set the log file path and name
LOGFILE="output.log"

#Set the email recipent
EMAIL= "kali@kali"

#Loop through the list of IP addresses or domains and ping each one
while read IP; do
	# Ping the IP and capture the output
	OUTPUT=$(ping -c 3 "$IP")
	#Parse the output to get the packet loss percentage
	PACKET_LOSS=$(echo "$OUTPUT" | grep -oP '\d+(?=% packet loss)')
	#Get the current timestamp
	TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
	#Check if the ping was successfull(packect loss = 0)
	if [[ "$PACKET_LOSS" == "0" ]]; then
		#Log the successful ping to the log file
		echo "$TIMESTAMP: $IP is online" >> "$LOGFILE"
	else
		#Log the unsuccessful ping to the log file
		echo "$TIMESTAMP: $IP is down ($PACKET_LOSS percent packet loss)"
	#Send the email to the system administrator
	mail -s "$IP is down" "$EMAIL" <<< "$OUTPUT"

	fi
done < "$1" 
