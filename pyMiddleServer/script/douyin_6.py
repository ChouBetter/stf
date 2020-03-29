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
		#'appPackage':app_package,
		#'appActivity':app_activity,
		'noReset':noreset_flag,
		'fullReset':fullreset_flag,
		'systemPort':systemPort,
		'wdaLocalPort': wdaLocalPort,	
		'unicodeKeyboard':'true',
		'resetKeyboard':'true'}
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
    
	def publish_comment(self,nums,times,duration):
		print('douyin comment test')
		print('[argument] [%s] nums = %d , times = %d , duration = %d' %(str(sys.argv[1]),nums,times,duration))
		
		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
		
		#執行 nums 次					
		for i in range(nums):	
			try:
				self.tap_for_locate();
				print('[  DEBUG ] 正在定位評論元素...')
				#點擊評論							
				comment=self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4e'))).click()
				print('[  DEBUG ] 正在定位輸入框元素...')
				#點擊輸入框	
				edit_text = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4_')))	
				edit_text.click()
				#評論 times 次			
				for j in range(times):
					#取得評論 
					text = self.get_comment()
					print('[  DEBUG ] comment = %s' %(text))
					print('[  DEBUG ] 正在定位輸入框元素...')
					#取得輸入框並輸入文字
					self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4_'))).send_keys(text)
					print('[  DEBUG ] 正在定位發送元素...')
					#點擊發送
					send = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4q'))).click()
					print('[  DEBUG ] 以評論 %d 次' %(j+1))
					time.sleep(duration)
				print('[  DEBUG ] 該用戶評論完畢，滑動至下一個用戶')
				#返回頁面
				self.driver.back();
				#向下滑動
				self.driver.swipe(x1, y2, x1, y1)							
			except:
				print '[ERROR] 無法定位元素' 
				#pass	
		
		print('======= [%s] douyin comment test finish ======' %(str(sys.argv[1])) )			         
	def main(self):
		self.publish_comment(1,1,3)
        	self.driver.quit()

M=Moments()
M.main()
