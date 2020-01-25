#!/bin/bash

# Check if IP is valid
con_ip1=`echo $1 | cut -d : -f 1 | cut -d . -f 4`

if [ ${con_ip1} -ge 50 ] && [ ${con_ip1} -le 84 ] || [ ${con_ip1} -ge 90 ] && [ ${con_ip1} -le 124 ] || [ ${con_ip1} -ge 130 ] && [ ${con_ip1} -le 164 ]; then
	adb disconnect $1
	sleep 1
	adb connect $1
else
	# Device ID out of range
	echo "Device IP out of range!"
	exit 1
fi

