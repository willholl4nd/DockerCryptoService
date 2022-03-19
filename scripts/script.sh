#!/bin/bash

#Start syslog-ng
service syslog-ng start

#Parse the ips from nmap and insert into main.cf and project.json
python3 parser.py

#Setup postfix
./postfixsetup.sh
cp /etc/resolv.conf /var/spool/postfix/etc/resolv.conf

#Run the script every minute
#Change the sleep time to run more or less frequently
while true; do
    sleep 60
    ./bin/main &
done
