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

    def auto_post_test(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Discover"]')))
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Moments"]')))
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/kj"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kj"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Choose from Album"]')))
        self.driver.find_element_by_xpath('//*[@text="Choose from Album"]').click()
        time.sleep(3)
#        self.driver.tap([(500,230)])
        self.driver.tap([(155,170)])
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/ki"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ki"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Say something..."]')))
        self.driver.find_element_by_xpath('//*[@text="Say something..."]').send_keys("Have a good vacation")
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Post"]')))
        self.driver.find_element_by_xpath('//*[@text="Post"]').click()
#        time.sleep(3)

    def main(self):
        self.auto_post_test()
        self.driver.quit()

M=Moments()
M.main()
