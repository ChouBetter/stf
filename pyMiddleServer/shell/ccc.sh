#!/bin/bash

ccc=`echo $1 | cut -d : -f 1 | cut -d . -f 4`
cluster_id=`echo $1 | cut -d : -f 1 | cut -d . -f 3`
echo ${ccc}
echo ${cluster_id}


if [ ${ccc} -ge 50 ] && [ ${ccc} -le 84 ]; then
	echo "AAAAA"
	ccc2=$((${ccc} + 40))
	ccc3=$((${ccc} + 80))
elif [ ${ccc} -ge 90 ] && [ ${ccc} -le 124 ]; then
	echo "BBBBB"
	ccc2=$((${ccc} - 40))
	ccc3=$((${ccc} + 40))
elif [ ${ccc} -ge 130 ] && [ ${ccc} -le 164 ]; then
	echo "CCCCC"
	ccc2=$((${ccc} - 40))
	ccc3=$((${ccc} - 80))
else
	echo "What are you doing?"
	exit 1
fi


echo ${ccc2}
echo ${ccc3}

con2="172.16."${cluster_id}"."${ccc2}
con3="172.16."${cluster_id}"."${ccc3}
echo ${con2}
echo ${con3}

