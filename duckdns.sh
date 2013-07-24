#!/bin/bash 
echo Starting the updater
while true; do
	export netname=$(tail /etc/hostname)
       export ducktoken=$(tail /home/pi/3dhome/ducktoken)
       echo Updating
	echo url="https://www.duckdns.org/create?domains="$netname"&token="$ducktoken"&ip=" | curl -k -o /home/pi/3dhome/duck.log -K -
	echo url="https://www.duckdns.org/update?domains=o"$netname"&token="$ducktoken"&ip=" | curl -k -o /home/pi/3dhome/duck.log -K -
       echo url="https://www.duckdns.org/update?domains=d"$netname"&token="$ducktoken"&ip=" | curl -k -o /home/pi/3dhome/duck.log -K -
	echo url="https://www.duckdns.org/update?domains=p"$netname"&token="$ducktoken"&ip=" | curl -k -o /home/pi/3dhome/duck.log -K -
       sleep 5m
done
