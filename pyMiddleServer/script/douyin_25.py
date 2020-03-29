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

	def get_fans_id(self, times=2):
		print('%s test'%(__file__))
		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8

		# print('[ DEBUG ] 正在定位首頁元素...')
		##點擊首頁頁面
		# try:
		# 	_ = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="首页"]'))).click()
		# except:
		# 	print('[ERROR] 無法點擊首頁元素')
		# 	return

		##暫停影片
		# self.driver.tap([(0,296),(720,1184)], 1000)

		#點擊直播主ID
		print('[ DEBUG ] 正在點擊直播主元素...')
		try:
			##背景有影片很慢
			# _ = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/title'))).click()
			el = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/title')
			el.click()
		except:
			print('[ERROR] 無法點擊直播主元素元素')
			return
		# el = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/title')
		# el.click()

		# #點擊直播主粉絲列表
		print('[ DEBUG ] 正在定位直播主粉絲列表元素...')
		try:
			##若直播中 很慢
			# _ = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/awt'))).click()
			el = self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/awt')
			el.click()
		except:
			print('[ERROR] 無法點擊直播主粉絲列表元素')
			return

		print("[ DEBUG ] 偵測是否有隱私設定")
		try:
			
		    _ = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/er7"]')))
		except:
			print('[ERROR] 有隱私設定!')
			return

		print("[ DEBUG ] 等待載入粉絲資料")
		try:
			_ = self.wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/f7w')))
		except:
			print('[ERROR] 無法載入粉絲資料!')
			return

		id_ls = []
		ac_ls = []
		total = 0
		while times > 0:
			##尋找目前頁面上所有的粉絲ID元素
			els = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/f7w')
			for el in els:
				account_name = el.text
				##略過相同的帳戶名稱
				if account_name in id_ls:
					pass
				else:
					##點擊ID進入ID頁面
					_ = el.click()
					try:
						account = self.wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/f_3')))
						id_ls.append(account_name)
						times -= 1
					except:
						print("[ERROR] 等待抖音號錯誤")
						break
					account_text = account.text
					account_text = account.text.encode('utf-8')
					account_text = account_text.split('抖音号：')[1]
					ac_ls.append(account_text)
					total += 1
					print("共蒐集了:%s個粉絲ID"%(total))

					##點擊返回按紐
					_ = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/ko'))).click()
				
				print("[ DEBUG ] 等待載入粉絲資料")
				try:
					_ = self.wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/f7w')))
				except:
					print('[ERROR] 無法載入粉絲資料!')
					break

				if times <= 0:
					break
			self.driver.swipe(x1, y2, x1, y1)
		self.driver.back()
		self.driver.back()
		
		# _ = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/ko'))).click()
		
		print('======= [%s] [%s] test finish ======' %(str(sys.argv[1]), __file__) )
		return ac_ls

	def main(self):
		ac_ls = self.get_fans_id(3)
		print(ac_ls)
		self.driver.quit()

M=Moments()
M.main()
