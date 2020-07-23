#!/bin/sh

LIST=$(ps aux|grep appium|grep adb|grep -v grep |awk '{print $2}')
for process in $LIST
do
    kill -9 $process
done
