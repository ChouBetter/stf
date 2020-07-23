#!/bin/sh

for i in $(seq 100 109)
do
python script/script5.py 172.16.2.$i:5555 &
done
