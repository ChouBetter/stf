# -*- coding: UTF-8 -*-
#----------------
# 功能 ： 指定關注並私信
# 參數設定 ：
wait_time = 3 #等待載入時間
duration_time = 1000 #點擊座標停留時間
# 執行格式 ： 檔名.py 機器名稱 對方ID 私訊內容（僅傳送一則訊息）
# 執行格式範例 ： python douyin_15.py 172.16.2.101:5555 xiaowumin4 hello
#----------------
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys

print str(sys.argv[1]) # 執行腳本機器名稱
print str(sys.argv[2]) # 對方ID
print str(sys.argv[3]) # 私訊內容

deviceName = sys.argv[1]
id_name = sys.argv[2]  # 對方ID
message = sys.argv[3]  # 私訊內容

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

        
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/ahv"]'))) #選取文字輸入欄位
        tab.send_keys(id_name)
        time.sleep(wait_time) #等待載入時間
        self.driver.press_keycode(84) #點擊 search key (KEYCODE_SEARCH)
        self.driver.press_keycode(66) #點擊 Enter key (KEYCODE_SEARCH)

        #---若有出現螢幕小鍵盤用此程式-----
        self.touch_tap(659,1126,duration_time) #點擊螢幕小鍵盤的scarch按鍵(通常在右下角)
        #------------------------------
        # #---若沒有出現螢幕小鍵盤用此程式---
        # time.sleep(wait_time) #等待載入時間
        # tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/f3b"]') #點擊 圖片
        # tab[0].click()        #點擊建議搜尋選項的第一項  
        #------------------------------

        time.sleep(wait_time) #等待載入時間
        time.sleep(wait_time) #等待載入時間
        
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/v0"]'))) #點擊 "關注"
        tab.click()

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/eoo"]'))) #點擊 "抖音號" 進入關注人個人主頁
        tab.click()

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dp2"]'))) #點擊 "私信"
        tab.click()
        
        self.touch_tap(360,1126,duration_time) #點擊下方文字輸入欄位

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/cfv"]'))) #選取文字輸入欄位
        tab.send_keys(message)
        
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/doq"]'))) #點擊 送出留言
        tab.click()

        self.touch_tap(30,104,duration_time) #點擊返回鍵 到關注人主頁

        self.touch_tap(30,104,duration_time) #點擊返回鍵 到搜尋頁面

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/f1e"]'))) #點擊 "取消" 將搜尋字串刪除
        tab.click()

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
