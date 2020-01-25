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
        self.wait=WebDriverWait(self.driver,10)

    def open_friends(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Contacts"]')))
        self.driver.find_element_by_xpath('//*[@text="Contacts"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@content-desc="More function buttons"]')))
        self.driver.find_element_by_xpath('//*[@content-desc="More function buttons"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Add Contacts"]')))
        self.driver.find_element_by_xpath('//*[@text="Add Contacts"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/d_4"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/d_4"]').click()

    def main(self):
        self.open_friends()
        self.driver.quit()

M=Moments()
M.main()
