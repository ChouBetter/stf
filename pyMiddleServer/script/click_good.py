from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

    def click_good(self):
        print('click_good test =======')

	timeout = WebDriverWait(self.driver, 2)

	tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="Discover"]'))).click()
	moments=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="Moments"]'))).click()

	tb=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@content-desc="You are in the page of,Moments"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]'))).size
	th=tb['height']

	s = self.driver.get_window_size()
	x1 = s['width'] * 0.25
	y1 = s['height'] * 0.25
	y2 = s['height'] * 0.5
	y2_i = s['height'] * 0.75
	self.driver.swipe(x1, y2, x1, y1)

	isEnd = False;

	while isEnd==False:

		items = self.driver.find_elements_by_xpath('//*[@content-desc="Comment"]')

		for item in items :
			try:
				ip = item.location
				if(ip['y']>th):
					item.click()
					like=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*/android.view.View/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')))
					isLike=like.get_attribute('text')
					print isLike
					if(isLike=="Like"):
						like.click()
			except:
				pass
		self.driver.swipe(x1, y2_i, x1, y1)
		try:
			endScroll = timeout.until_not(EC.element_to_be_clickable((By.XPATH,'//android.widget.FrameLayout[@content-desc="You are in the page of,Moments"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout')))
		except :
			isEnd = True;
			print 'Scroll End!';

	items = self.driver.find_elements_by_xpath('//*[@content-desc="Comment"]')

	for item in items :
		try:
			ip = item.location
			if(ip['y']>th):
 				item.click()
                                like=timeout.until(EC.element_to_be_clickable((By.XPATH,'//*/android.view.View/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')))
                                isLike=like.get_attribute('text')
				print isLike
				if(isLike=="Like"):
					like.click();
		except:
			pass


	print 'click_good finish ======'
    def main(self):
        self.click_good()
        self.driver.quit()

M=Moments()
M.main()
