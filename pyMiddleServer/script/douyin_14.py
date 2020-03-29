# -*- coding: UTF-8 -*-
#----------------
# 功能 ： 指定刷讚（會透過ORcode圖片搜尋對方,必須預先把ORcode圖片放到像不裏面）(將會刷整支帳號的貼文)
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
        self.touch_tap(659,80,duration_time)#點擊 搜尋符號

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/nw"]'))) #點擊 掃描QRCode按鈕
        tab.click()

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dre"]'))) #點擊 "相冊"
        tab.click()

        time.sleep(wait_time) #等待載入時間
        time.sleep(wait_time) #等待載入時間
        tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/a0d"]') #點擊 圖片
        tab[num_picture].click()   

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/x9"]'))) #點擊 "確定"
        tab.click()

        time.sleep(wait_time) #等待載入時間
        time.sleep(wait_time) #等待載入時間
        time.sleep(wait_time) #等待載入時間

        # tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dp2"]'))) #點擊 "私信"
        # tab.click()
        
        #--------------------
        # 進行整之帳號的刷讚
        #--------------------
        n = 0 #初始化
        while(True):
            
            try :
                time.sleep(wait_time) #等待載入時間
                tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/ah"]') #點擊進入 好友的貼文
                tab[n].click()
                n += 1                #逐一點讚
                
                self.touch_tap(659,602,duration_time) #點擊愛心

                self.touch_tap(30,104,duration_time) #點擊返回鍵
            except:
                print('刷讚完成')
                break

        self.touch_tap(30,104,duration_time) #點擊返回鍵,返回發現好友

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/f1e"]'))) #點擊 "取消" 返回主頁
        tab.click()

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
