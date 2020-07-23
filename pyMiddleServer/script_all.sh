#!/bin/sh

for i in $(seq 130 159)
do
python script/script5.py 172.16.2.$i:5555 &
done
sleep 2
for i in $(seq 90 119)
do
python script/script5.py 172.16.2.$i:5555 &
done
