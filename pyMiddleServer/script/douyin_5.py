# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys

print str(sys.argv[1])
deviceName = sys.argv[1]

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
#        	'appPackage':app_package,
#        	'appActivity':app_activity,
        	'noReset':noreset_flag,
        	'fullReset':fullreset_flag,
        	'systemPort':systemPort,
        	'wdaLocalPort': wdaLocalPort}
        	self.driver=webdriver.Remote(driver_server,self.desired_caps)
        	self.wait=WebDriverWait(self.driver,300)
	
	#點擊頁面一次確保元素可以被定位
    	def tap_for_locate(self):
		#time.sleep(2)
		self.driver.tap([(0,296),(720,1184)], 500)
    
	def notify(self,times):
		print('douyin notify fans test')
		print('[argument] [%s] times = %d' %(str(sys.argv[1]),times))
		
		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.2
		x2 = s['width'] * 0.8
		y1 = s['height'] * 0.5

		self.tap_for_locate()
		#向右滑動
		self.driver.swipe(x2, y1, x1, y1)
		print('[  DEBUG ] 正在定位粉絲元素...')
		#點擊粉絲
		notifyTab = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/awv'))).click()
		
		print('[  DEBUG ] 正在定位關注元素...')
		items = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/v0')))
		#取得頁面上的關注按鈕
		items = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/v0')

		#畫面上出現的按鈕數量							
		scrollLimit = 6
		cnt = 0

		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
		
		for item in items :
			#取得該按鈕的文字
			isNotify = item.get_attribute('text')	
			if isNotify == u'关注':
				item.click()				
				cnt+=1
				print('[  DEBUG ] 以點擊 %d 次關注' %(cnt))
			#如果已經操作到最後一個按鈕就向下滑動
			if cnt%scrollLimit==0 :
				self.driver.swipe(x1, y2, x1, y1)
			#如果已經點擊足夠次數就終止	
			if cnt == times:
				break								      				

		print('======= [%s] douyin notify fans test finish ======' %(str(sys.argv[1])) )			         
	def main(self):
		self.notify(2)
        	self.driver.quit()

M=Moments()
M.main()
