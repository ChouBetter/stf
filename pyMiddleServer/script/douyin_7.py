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
        	'wdaLocalPort': wdaLocalPort,
		'unicodeKeyboard':'true',
		'resetKeyboard':'true'}
        	self.driver=webdriver.Remote(driver_server,self.desired_caps)
        	self.wait=WebDriverWait(self.driver,300)

	#點擊頁面一次確保元素可以被定位
    	def tap_for_locate(self):
		#time.sleep(2)
		self.driver.tap([(0,296),(720,1184)], 1000)
    
	def forward(self,title):
		print('douyin forward test')
		print('[argument] [%s] title = %s' %(str(sys.argv[1]),title))

		self.tap_for_locate();		
		print('[  DEBUG ] 正在定位分享元素...')
		#點擊分享							
		share=self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/dr3'))).click()
		print('[  DEBUG ] 正在定位轉發元素...')
		#點擊轉發
		forward=self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/dqg'))).click()
		print('[  DEBUG ] 正在定位輸入框元素...')
		#點擊輸入框
		edit_text = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4_')))	
		edit_text.click()
		#將文字送至輸入框
		self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a4_').send_keys(title)
		print('[  DEBUG ] 正在定位發送元素...')
		#點擊發送
		send = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/a4q'))).click()
										      				
		print('======= [%s] douyin forward  test finish ======' %(str(sys.argv[1])) )		         
	def main(self):
		self.forward(u'转发')
        	self.driver.quit()

M=Moments()
M.main()
