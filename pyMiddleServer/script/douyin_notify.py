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
    
	def notify(self,times):
		print('douyin notify test ======= [argument] times = %d' %(times))

		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
					
		for i in range(times):	
			try: 
				self.tap_for_locate();							
				notify=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/aw2"]'))).click()
				print('douyin notify test ======= [  DEBUG ] click notify cnt = %d' %(i+1))
				self.driver.swipe(x1, y2, x1, y1)
							
			except:
				print 'douyin notify test ======= [ERROR]' 
				pass	
			      				

		print('douyin notify test ======= finish ======')

    def main(self):
        self.notify(2)
        self.driver.quit()

M=Moments()
M.main()
