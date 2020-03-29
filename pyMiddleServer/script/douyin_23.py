# -*- coding: UTF-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys
from selenium.common.exceptions import NoSuchElementException

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

	##點擊返回
	def click_return(self):
		_ = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@content-desc="返回"]'))).click()


	##點擊我->
	def findFriends(self):

		print('%s test'%(__file__))

		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8

		print('[ DEBUG ] 正在定位我元素...')
		##點擊我頁面
		try:
			_ = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="我"]'))).click()
		except:
			print('[ERROR] 無法點擊我元素')
			return

		#點擊 +好友
		print('[ DEBUG ] 正在定位+好友元素...')
		try:
			_ = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="好友"]'))).click()
		except:
			print('[ERROR] 無法點擊+好友元素')
			return

		#等待 好友列表
		print('[ DEBUG ] 正在定位好友列表元素...')
		try:
			_ = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="好友列表"]')))
		except:
			print('[ERROR] 無法定位好友列表元素')
			self.click_return()
			return

		#判斷是否有推薦好友
		try: 
			_ = self.driver.find_element_by_xpath('//*[@text="暂无好友推荐"]')
			print("[ DEBUG ] 目前暫無好友推薦")
			self.click_return()
			return
		except NoSuchElementException:
			pass

		#尋找 關注 按紐
		print('[ DEBUG ] 正在定位關注元素...')
		try:
			##等待至少一個關注出現
			_ = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="关注"]')))
		except:
			print('[ERROR] 無法定位關注元素')
			self.click_return()
			return
		##尋找目前頁面上所有的關注元素
		total = 0
		while True:
			els = self.driver.find_elements_by_xpath('//*[@text="关注"]')
			for el in els:
				el.click()
				total += 1

			##檢測是否到最底
			try:
				self.driver.find_element_by_xpath('//*[@text="没有更多了"]')
				break
			except NoSuchElementException:
				##若無則繼續往下滑
				self.driver.swipe(x1, y2, x1, y1)

		print("[ DEBUG ]共新增了[%s]位關注" %(total))
		self.click_return()

		print('======= [%s] [%s] test finish ======' %(str(sys.argv[1]), __file__) )

	def main(self):
		self.findFriends()
		self.driver.quit()

M=Moments()
M.main()
