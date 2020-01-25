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
driver_server='http://localhost:54723/wd/hub'
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
        self.driver.activate_app('com.tencent.mm');
        time.sleep(8)
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
        time.sleep(5)
        self.driver.terminate_app('com.tencent.mm');
#        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kx"]').click()
#        self.driver.press_keycode(4)
#        time.sleep(3)

    def main(self):
#        self.login()
#        self.enter()
        self.click_test()
        self.driver.quit()

M=Moments()
M.main()
