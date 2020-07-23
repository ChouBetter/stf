#!/bin/sh

LIST=$(ps aux|grep appium|grep node|grep -v grep |awk '{print $2}')
for process in $LIST
do
    kill $process
done
