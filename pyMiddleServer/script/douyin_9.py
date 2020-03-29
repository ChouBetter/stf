# -*- coding: UTF-8 -*-
#----------------
# 功能 ： 評論好友作品
# 參數設定 ：
wait_time = 3 #等待載入時間
duration_time = 1000 #點擊座標停留時間
# 執行格式 ： 檔名.py 機器名稱 好友數量 評論數量 評論次數 評論時間間隔(秒) 評論內容
#----------------
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys

print str(sys.argv[1]) # 執行腳本機器名稱
print str(sys.argv[2]) # 好友數量
print str(sys.argv[3]) # 評論數量
print str(sys.argv[4]) # 評論次數
print str(sys.argv[5]) # 評論時間間隔(秒)
print str(sys.argv[6]) # 評論內容

deviceName = sys.argv[1]
num_firends = int(sys.argv[2]) # 好友數量
num_post = int(sys.argv[3])    # 評論數量
num_times = int(sys.argv[4])   # 評論次數
num_delay = int(sys.argv[5])   # 評論時間間隔(秒)
message_content = sys.argv[6]  # 評論內容

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

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="好友列表"]'))) #點擊 "好友列表"
        tab.click()

        for m in range(num_firends) : #依照輸入數量去對幾位好友按讚
            print 'num_friend :',m
            try :
                if m != 0 and m % 7 == 0 :         #每完成7個項目 頁面須往下移動
                    self.swipeUp(1000) #向上滑動
                    print('頁面往下捲動')

                time.sleep(wait_time) #等待載入時間
                tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/a3c"]') #點擊進入 好友的主頁
                tab[m].click()

                for n in range(num_post) : #依照輸入數量去對幾篇文流言
                    print 'num_post :',n
                    try :
                        if n != 0 and n % 3 == 0 :         #每完成3個項目 頁面須往下移動
                            self.swipeUp(1000) #向上滑動
                            print('頁面往下捲動')

                        time.sleep(wait_time) #等待載入時間
                        tab=self.driver.find_elements_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/ah"]') #點擊進入 好友的貼文
                        tab[n].click()
                        
                        self.touch_tap(659,746,duration_time) #點擊評論
                        
                        for u in range(num_times) : #依照輸入數量留言
                            self.touch_tap(55,1126,duration_time) #點擊下方留言欄位(當非第1則留言會點到鍵盤但不影響運作)
                            tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a4_"]'))) #選取文字輸入欄位
                            tab.send_keys(message_content)

                            tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a4q"]'))) #點擊 送出留言
                            tab.click()

                            time.sleep(num_delay) #重複留言的時間間隔
                        
                        self.touch_tap(30,104,duration_time) #點擊返回

                        self.touch_tap(30,104,duration_time) #點擊返回鍵
                    except:
                        print('超過現有的貼文數量')
                        break

                self.touch_tap(30,104,duration_time) #點擊返回鍵,返回好友列表

            except:
                        print('超過實際好友數量')
                        break

        self.touch_tap(55,92,duration_time) #點擊返回鍵,返回個人主頁

        self.touch_tap(55,1126,duration_time) #點擊首頁

        #self.driver.quit()
    
    def touch_tap(self,x,y,duration=100): #螢幕點擊座標  ,x1,x2,y1,y2,duration
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
