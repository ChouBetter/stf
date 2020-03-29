# -*- coding: UTF-8 -*-
#----------------
# 功能 ： 互相關注（透過ORcode圖片加對方好友,必須預先把ORcode圖片放到像不裏面）
# 參數設定 ：
wait_time = 3 #等待載入時間
duration_time = 1000 #點擊座標停留時間
# 執行格式 ： 檔名.py 機器名稱 QRcode相簿第幾張照片(從0開始數)
#----------------
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys

print str(sys.argv[1]) # 執行腳本機器名稱
print str(sys.argv[2]) # 選擇 QRcode相簿第幾張照片

deviceName = sys.argv[1]
num_picture = int(sys.argv[2])  # QRcode相簿第幾張照片


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
        self.touch_tap(659,1126,duration_time)#點擊 "我"

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/eo3"]'))) #點擊 "+好友"
        tab.click()

        time.sleep(wait_time) #等待載入時間
        tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/azp"]') #點擊 "掃一掃"
        tab[2].click() 

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dre"]'))) #點擊 "相冊"
        tab.click()

        time.sleep(wait_time) #等待載入時間
        tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/a0d"]') #點擊 圖片
        tab[num_picture].click()   

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/x9"]'))) #點擊 "確定"
        tab.click()

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/d3k"]'))) #點擊 "關注"
        tab.click()

        self.touch_tap(30,104,duration_time) #點擊返回鍵,返回發現好友

        self.touch_tap(55,92,duration_time) #點擊返回鍵,返回個人主頁

        self.touch_tap(55,1126,duration_time) #點擊首頁

        #self.driver.quit()

    def touch_tap(self,x,y,duration=100):   #點擊座標  ,x1,x2,y1,y2,duration
        time.sleep(wait_time) #等待載入時間
        '''
        method explain:點擊座標
        parameter explain：【x,y】座標值,【duration】:給的值決定了點擊的速度
        Usage:
            device.touch_coordinate(277,431)      #277.431爲點擊某個元素的x與y值
        '''
        screen_width = self.driver.get_window_size()['width']  #獲取當前屏幕的寬
        screen_height = self.driver.get_window_size()['height']   #獲取當前屏幕的高
        a =(float(x)/screen_width)*screen_width
        x1 = int(a)
        b = (float(y)/screen_height)*screen_height
        y1 = int(b)
        self.driver.tap([(x1,y1),(x1,y1)],duration)

M=Moments()
M.main()
