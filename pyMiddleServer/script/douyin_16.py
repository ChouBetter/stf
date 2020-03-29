# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys
import random

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
		'automationName': "UiAutomator2",
        	'noReset':noreset_flag,
        	'fullReset':fullreset_flag,
        	'systemPort':systemPort,
        	'wdaLocalPort': wdaLocalPort}
        	self.driver=webdriver.Remote(driver_server,self.desired_caps)
        	self.wait=WebDriverWait(self.driver,300)

	#點擊頁面一次確保元素可以被定位
	def tap_for_locate(self):
		#time.sleep(2)
		self.driver.tap([(0,296),(720,1184)], 1000)
	
	#隨機挑選一則評論
	def get_comment(self):
		comments = [
			u'很有趣',
			u'转发',
			u'这个我喜欢'
		]
		return random.choice(comments)
    
	def publish_comment(self):
		print('douyin comment test')
		print('[argument] [%s] ' %(str(sys.argv[1])))
		
		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
		
		self.driver.swipe(x1, y2, x1, y1)	
		
		try:
			self.tap_for_locate();
			
			#取得評論 
			#text = self.get_comment()
			#print('[  DEBUG ] comment = %s' %(text))
			print('[  DEBUG ] 正在定位搜索元素...')
			#點擊搜索							
			search=self.wait.until(EC.element_to_be_clickable((By.ID,"com.ss.android.ugc.aweme:id/bi8"))).click()
			#search = self.wait.until(EC.presence_of_element_located((By.ID, "com.ss.android.ugc.aweme:id/c3w"))).click()		
			#self.driver.tap([(636,58),(708,130)], 1000)
			print('[  DEBUG ] 正在定位掃一掃元素...')
			#點擊掃一掃	
			swipe = self.wait.until(EC.element_to_be_clickable((By.ID,"com.ss.android.ugc.aweme:id/nw"))).click()
			print('[  DEBUG ] 正在定位相冊元素...')
			#點擊相冊
			album = self.wait.until(EC.element_to_be_clickable((By.ID,"com.ss.android.ugc.aweme:id/dre"))).click()
			print('[  DEBUG ] 正在定位選擇元素...')
			#點擊選擇
			select = self.wait.until(EC.element_to_be_clickable((By.ID,"com.ss.android.ugc.aweme:id/a0d"))).click()
			print('[  DEBUG ] 正在定位確認元素...')
			#點擊確認
			confirm = self.wait.until(EC.element_to_be_clickable((By.ID,"com.ss.android.ugc.aweme:id/x9"))).click()							
											
		except:
			print '[ERROR] 無法定位元素' 
			#pass	
		
		print('======= [%s] douyin comment test finish ======' %(str(sys.argv[1])) )
    	
	def main(self):
		self.tap_for_locate();
		self.publish_comment()	
		self.driver.quit()

M=Moments()
M.main()
