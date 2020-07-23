#!/bin/sh

ps aux | grep appium | grep node | awk '{print $2}' | xargs kill -9
ps aux | grep appium | grep adb | awk '{print $2}' | xargs kill -9
ps aux | grep appium
