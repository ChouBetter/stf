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
		time.sleep(2)
		self.driver.tap([(0,296),(720,1184)], 1000)

	def test(self):
		print('douyin_22 test')

		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8

		print('[ DEBUG ] 正在定位消息元素...')
		##點擊消息頁面
		
		msg=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="消息"]'))).click()
		

		# try:
		# 	msg=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="消息"]')))
		# 	print(msg)
		# except:
		# 	print('[ERROR] 無法定位消息元素' )
		# 	return
		print('======= [%s] [%s] test finish ======' %(str(sys.argv[1]), __file__) )

	def main(self):
		# self.tap_for_locate()
		self.test()
		self.driver.quit()

M=Moments()
M.main()
