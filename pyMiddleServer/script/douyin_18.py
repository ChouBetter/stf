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
		self.driver.tap([(0,296),(720,1184)], 1000)
    
	def mail_fans(self,content,times,duration):
		print('douyin_18 test ======= ')
		print('[argument] [%s] content.length = %d , times = %d , duration = %d' %(str(sys.argv[1]),len(content),times,duration))

		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
		
		try:	
			print('[  DEBUG ] 正在定位我元素...')		
			#點擊同城頁面
			me=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="我"]'))).click()
			print('[  DEBUG ] 正在定位關注元素...')
			#點擊關注頁面
			notify = self.wait.until(EC.presence_of_element_located((By.ID, "com.ss.android.ugc.aweme:id/awv"))).click()
			
			print('[  DEBUG ] 正在定位用戶元素...')
			users = self.wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/f7w')))				
			#取得頁面上的關注按鈕
			users = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/f7w')

			#畫面上出現的按鈕數量							
			scrollLimit = 6
			cnt = 0	
			for user in users :
				user.click()
				print('[  DEBUG ] 正在定位私信元素...')
				#點擊私信
				notify = self.wait.until(EC.presence_of_element_located((By.ID, "com.ss.android.ugc.aweme:id/dp4"))).click()
				for text in content :
					print('[  DEBUG ] text = %s' %(text))
					print('[  DEBUG ] 正在定位輸入框元素...')
					#取得輸入框並輸入文字
					self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/cfv'))).send_keys(text)
					print('[  DEBUG ] 正在定位發送元素...')
					#點擊發送
					send = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/doq'))).click()
					cnt+=1
					print('[  DEBUG ] 以評論 %d 次' %(cnt))
				print('[  DEBUG ] 該用戶私信完畢，滑動至下一個用戶')								
				self.driver.back()
				self.driver.back()
				time.sleep(duration)				
				if cnt%scrollLimit==0 :
					self.driver.swipe(x1, y2, x1, y1)
				#如果已經私信足夠次數就終止	
				if cnt == times:
					#break	
						
		except:
			print '[ERROR] 無法定位元素' 
			pass	
			      				
		print('======= [%s] douyin_18 test finish ======' %(str(sys.argv[1])) )

	def main(self):
		self.tap_for_locate()
		self.mail_fans(['hi~'],1,10)
		self.driver.quit()

M=Moments()
M.main()
