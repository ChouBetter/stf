# -*- coding: UTF-8 -*-
#----------------
# 功能 ： 刷抖音
# 參數設定 ：
wait_time = 3 #等待載入時間
duration_time = 1000 #點擊座標停留時間
# 執行格式 ： 檔名.py 機器名稱 刷文數量 刷文時間間隔(秒)
#----------------
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys

print str(sys.argv[1]) # 執行腳本機器名稱
print str(sys.argv[2]) # 刷文數量
print str(sys.argv[3]) # 刷文時間間隔(秒)

deviceName = sys.argv[1]
num_swipe = int(sys.argv[2])  # 刷文數量
num_delay = int(sys.argv[3])  # 刷文時間間隔(秒)

PLATFORM='Android'
app_package='com.ss.android.ugc.aweme'
app_activity='.main.MainActivity'
driver_server='http://localhost:24723/wd/hub'
noreset_flag='true'
fullreset_flag='false'
serverSerial = int(deviceName.split(':', 1)[0].split('.')[3])
systemPort = str(serverSerial * 100 + 5)
wdaLocalPort = str(serverSerial * 100 + 10)

class Moments():
    def __init__(self):
        self.desired_caps={
		'platformName':PLATFORM,
    	'deviceName':deviceName,
    	'udid':deviceName,
       	'appPackage':app_package,
       	'appActivity':app_activity,
       	'noReset':noreset_flag,
       	'fullReset':fullreset_flag,
       	'systemPort':systemPort,
       	'wdaLocalPort': wdaLocalPort}
       	self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)
        
    def main(self):
        time.sleep(wait_time) #等待載入時間

        for m in range(num_swipe) : #依照輸入數量去對幾位好友按讚
            time.sleep(num_delay) #等待時間
            self.swipeUp(1000) #向上滑動

        #self.driver.quit()

    def getSize(self): #獲得機器螢幕大小x,y
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self,t): #螢幕向上滑動
        time.sleep(wait_time) #等待載入時間
        l = self.getSize()
        x1 = int(l[0] * 0.5)  #x座標
        y1 = int(l[1] * 0.75)   #起始y座標
        y2 = int(l[1] * 0.25)   #終點y座標
        self.driver.swipe(x1, y1, x1, y2,t)
    
    def swipeDown(self,t): #螢幕向下滑動
        time.sleep(wait_time) #等待載入時間
        l = self.getSize()
        x1 = int(l[0] * 0.5)  #x座標
        y1 = int(l[1] * 0.25)   #起始y座標
        y2 = int(l[1] * 0.75)   #終點y座標
        self.driver.swipe(x1, y1, x1, y2,t)
    
    def swipLeft(self,t): #螢幕向左滑動
        time.sleep(wait_time) #等待載入時間
        l= self.getSize()
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.05)
        self.driver.swipe(x1,y1,x2,y1,t)
    
    def swipRight(self,t): #螢幕向右滑動
        time.sleep(wait_time) #等待載入時間
        l= self.getSize()
        x1=int(l[0]*0.05)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1,y1,x2,y1,t)

M=Moments()
M.main()
