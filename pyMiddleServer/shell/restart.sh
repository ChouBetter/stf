#!/bin/bash

# Check if IP is valid
con_ip1=`echo $1 | cut -d : -f 1 | cut -d . -f 4`
cluster_id=`echo $1 | cut -d : -f 1 | cut -d . -f 3`

if [ ${con_ip1} -ge 50 ] && [ ${con_ip1} -le 84 ] || [ ${con_ip1} -ge 90 ] && [ ${con_ip1} -le 124 ] || [ ${con_ip1} -ge 130 ] && [ ${con_ip1} -le 164 ]; then
	# Disconnect Device
	adb disconnect $1
	sleep 1

	sshpass -p vmivmi ssh -o StrictHostKeyChecking=no -t -t vmi@172.16.0.10 "/home/vmi/vmi-mng-db/action_test_restart_con 2 $1"

	sleep 40

	# Device reconnect
#	if [ ${con_ip1} -ge 50 ] && [ ${con_ip1} -le 84 ]; then
#		con_ip2=$((${con_ip1} + 40))
#		con_ip3=$((${con_ip1} + 80))
#	elif [ ${con_ip1} -ge 90 ] && [ ${con_ip1} -le 124 ]; then
#		con_ip2=$((${con_ip1} - 40))
#		con_ip3=$((${con_ip1} + 40))
#	elif [ ${con_ip1} -ge 130 ] && [ ${con_ip1} -le 164 ]; then
#		con_ip2=$((${con_ip1} - 40))
#		con_ip3=$((${con_ip1} - 80))
#	else
#		echo "What are you doing?"
#		exit 1
#	fi
#
#	con2="172.16."${cluster_id}"."${con_ip2}
#	con3="172.16."${cluster_id}"."${con_ip3}

	adb connect $1
#	adb connect ${con2}
#	adb connect ${con3}
else
	# Device ID out of range
	echo "Device IP out of range!"
	exit 1
fi

