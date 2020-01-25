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
#        'appPackage':app_package,
#        'appActivity':app_activity,
        'noReset':noreset_flag,
        'fullReset':fullreset_flag,
        'systemPort':systemPort,
        'wdaLocalPort': wdaLocalPort}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)

    def tap_for_locate(self):
		s = self.driver.get_window_size()
		x_cent = s['width'] * 0.5
        y_cent = s['height'] * 0.5
		time.sleep(2)
		self.driver.tap([(0,0),(720,1184)], 500)

	def get_comment(self):
		comments = [
			u'很有趣',
			u'转发',
			u'这个我喜欢'
		]
		return random.choice(comments)
    
	def publish_comment(self,nums,times,duration):
		print('douyin comment test ======= [argument] nums = %d , times = %d , duration = %d' %(nums,times,duration))

		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
					
		for i in range(nums):	
			try:
				self.tap_for_locate();							
				comment=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a3r"]'))).click()
				edit_text = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a3m"]')))	
				edit_text.click()			
				for j in range(times): 
					text = self.get_comment()
					print('douyin comment test ======= [  DEBUG ] comment = %s' %(text))
					self.driver.find_element_by_xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/a3m"]').send_keys(text)
					send = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/a43"]'))).click()
					print('douyin comment test ======= [  DEBUG ] comment send times = %d' %(j))
					time.sleep(duration)
				print('douyin comment test ======= [  DEBUG ] comment publish successed,ready swipe to next')
				self.driver.back();
				self.driver.swipe(x1, y2, x1, y1)							
			except:
				print 'douyin comment test ======= [ERROR]' 
				pass	
			      				
		print('douyin comment test ======= finish ======')			         
	def main(self):
		self.publish_comment(1,1,3)
        self.driver.quit()

M=Moments()
M.main()
