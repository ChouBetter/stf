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
	
	def notify(self,douyin_nums,times):
		print('douyin notify test')
		print('[argument] [%s] douyin_nums.length = %d , times = %d' %(str(sys.argv[1]),len(douyin_nums),times))
		
		#取得頁面大小
		s = self.driver.get_window_size()
		x1 = s['width'] * 0.5
		y1 = s['height'] * 0.2
		y2 = s['height'] * 0.8
		
		#self.tap_for_locate()
		#self.driver.swipe(x1, y2, x1, y1)	
		self.tap_for_locate()
		print('[  DEBUG ] 正在定位搜索元素...')
		#點擊搜索							
		search=self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/bi8'))).click()
		
		for douyin_number in douyin_nums :
			try:						
				#取得評論 
				print('[  DEBUG ] douyin_number = %s' %(douyin_number))
				
				print('[  DEBUG ] 正在定位輸入框元素...')
				#取得輸入框並輸入文字
				self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/ahv'))).clear().send_keys(douyin_number)
				print('[  DEBUG ] 正在定位列表元素...')
				#點擊列表
				search_list = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/f3b'))).click()
				print('[  DEBUG ] 正在定位用戶元素...')
				#點擊用戶
				user = self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/buz'))).click()
				
				print('[  DEBUG ] 正在定位粉絲元素...')
				#點擊粉絲
				notifyTab=self.wait.until(EC.element_to_be_clickable((By.ID,'com.ss.android.ugc.aweme:id/awv'))).click()
							
				#time.sleep(2)
                                #self.tap_for_locate()
				print('[  DEBUG ] 正在定位關注元素...')
				items = self.wait.until(EC.presence_of_element_located((By.ID,'com.ss.android.ugc.aweme:id/v0')))				
				#取得頁面上的關注按鈕
				items = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/v0')

				#畫面上出現的按鈕數量							
				scrollLimit = 6
				cnt = 0	
				for item in items :
					#取得該按鈕的文字
					isNotify = item.get_attribute('text')
					print('[  DEBUG ] text = %s' %(isNotify))	
					if isNotify == u'关注':
						item.click()				
						cnt+=1
						print('[  DEBUG ] 以點擊 %d 次關注' %(cnt))
					#如果已經操作到最後一個按鈕就向下滑動
					if cnt%scrollLimit==0 :
						self.driver.swipe(x1, y2, x1, y1)
					#如果已經點擊足夠次數就終止	
					if cnt == times:
						break							
				#返回頁面
				self.driver.back()
				self.driver.back()
				self.driver.back()						
			except:
				print '[ERROR] 無法定位元素' 
				#pass	
		
		print('======= [%s] douyin notify test finish ======' %(str(sys.argv[1])) )
	
	def main(self):
		self.notify(['dxz3838438'],1)
		self.driver.quit()

M=Moments()
M.main()
