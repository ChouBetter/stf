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
driver_server='http://123.51.133.103:24723/wd/hub'
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

    	def tap_for_locate(self):
		time.sleep(1)
		self.driver.tap([(0,296),(720,1184)], 500)
		time.sleep(1)
    
	def forward(self,title):
		print('tiktok forward test ======= [argument] title = %s' %(title))

		self.tap_for_locate();							
		share=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dr3"]'))).click()
		forward=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/dqg"]'))).click()

		edit_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a4_"]')))	
		edit_text.click()
		self.driver.find_element_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/a4_"]').send_keys(title)
		send = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a4q"]'))).click()
										      				
		print('tiktok forward test ======= finish ======')			         
	def main(self):
		self.forward(u'转发')
        	self.driver.quit()

M=Moments()
M.main()
