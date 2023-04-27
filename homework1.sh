!#/bin/bash

# set an array of addresses to ping

addresses=(www.google.com www.youtube.com www.netflix.com "58.96.36.1")

# loop through the addresses and ping each one

for address in "${addresses[@]}"

do

  echo "Pinging $address..."

  ping -c 4 $address

done

# ping the NetID address (replace with your own NetID)

netid="58.96.36.1"

echo "Pinging NetID address $netid..."

ping -c 4 $netid


#Question 2
# set an array of addresses to ping

addresses=(www.google.com www.youtube.com www.Netflix.com "58.96.36.1")

# set a variable for the log file name

log_file="input.txt"

 

# loop through the addresses and ping each one, logging the output

for address in "${addresses[@]}"

do

  echo "$(date): Pinging $address..." >> $log_file

  ping -c 4 $address >> $log_file


done

# ping the NetID address (replace with your own NetID), logging the output

netid="58.96.36.1"

echo "$(date): Pinging NetID address $netid..." >> $log_file

ping -c 4 $netid >> $log_file


#Question 3

# set the email address to receive notifications

email="kali@kali"

#set an array of addresses to ping

addresses=(www.google.com www.youtube.com www.Netflix.com "58.96.36.1")

# loop through the addresses and ping each one

for address in "${addresses[@]}"

do

  if ping -c 4 $address >/dev/null 2>&1

  then

    echo "Ping to $address succeeded"

  else

    echo "Ping to $address failed"

    echo "Ping to $address failed at $(date)" | mail -s "Ping failure for $address" $email

  fi

done


