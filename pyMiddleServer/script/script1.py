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
app_package='com.tencent.mm'
app_activity='.ui.LauncherUI'
driver_server='http://localhost:24723/wd/hub'
noreset_flag='true'
fullreset_flag='false'

class Moments():
    def __init__(self):
        self.desired_caps={
        'platformName':PLATFORM,
        'deviceName':deviceName,
        'udid':deviceName,
#        'appPackage':app_package,
#        'appActivity':app_activity,
        'noReset':noreset_flag,
        'fullReset':fullreset_flag}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)

    def login(self):
        print('login test ======')

    def enter(self):
        print('click find ======')
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/cdh"]/..')))
        print('find the find =====')
        time.sleep(6)
        tab.click()
        print('click friend =====')
        friends=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="android:id/list"]/*[@class="android.widget.LinearLayout"][1]')))
        friends.click()
    
    def swipe_test(self):
        print('swipe test ======')
        time.sleep(5)
        self.driver.swipe(start_x=100, start_y=500, end_x=300, end_y=500, duration=100)

    def click_test(self):
        print('click test ======')
        time.sleep(8)
#        self.driver.activate_app('com.tencent.mm');
#        time.sleep(8)
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
        time.sleep(5)
#        self.driver.terminate_app('com.tencent.mm');
#        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kx"]').click()
#        self.driver.press_keycode(4)
#        time.sleep(3)
    def nearby_test(self):
        print('nearby test =======')

	tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView'))).click()
	#tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="Discover"]'))).click()
	time.sleep(3)

	friends=self.driver.find_element_by_xpath('//*[@text="People Nearby"]').click()
	time.sleep(3)

	alert = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@text="OK"]'))).click()

	#search=self.driver.find_element_by_xpath('//*[@text="Search"]').click()
        #time.sleep(3)

    def click_good_test(self):
	print('click_good test =======')

        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/tb"]'))).click()
	moments=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="Moments"]'))).click()

	s = self.driver.get_window_size()
	x1 = s['width'] * 0.25
	y1 = s['height'] * 0.25
	y2 = s['height'] * 0.5
	y2_i = s['height'] * 0.75
	self.driver.swipe(x1, y2, x1, y1)

	isEnd = False;
	timeout = WebDriverWait(self.driver, 2)

	while isEnd==False:

		items = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/eyz"]')

		for item in items :
			try:
				item.click()
				like=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/eyk"]')))
				isLike=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/eym"]'))).get_attribute('text')
				print isLike
				if(isLike=="Like"):
					like.click();
			except:
				pass

		self.driver.swipe(x1, y2_i, x1, y1)
		try:
			endScroll = timeout.until_not(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/aly"]')))
		except :
			isEnd = True;
			print 'Scroll End!';

	items = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/eyz"]')

	for item in items :
		try:
			item.click()
			like=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/eyk"]')))
			isLike=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/eym"]'))).get_attribute('text')
			print isLike
			if(isLike=="Like"):
				like.click()
		except:
			pass

    def main(self):
#       self.login()
#       self.enter()
        self.click_good_test()
        self.driver.quit()

M=Moments()
M.main()

