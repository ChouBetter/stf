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

time_sleep = 1.5 # Delay Time

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

    def main(self):

        try : 
            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@text="Contacts"]').click()
            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@text="New Friends"]').click()
            time.sleep(time_sleep)

            back = True
            while back is True :
                try:
                    self.driver.find_element_by_xpath('//*[@text="Accept"]').click()
                    #self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/c1y"]').click()
                    time.sleep(time_sleep)
                    self.driver.find_element_by_xpath('//*[@text="Done"]').click()
                    #self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ln"]').click()
                    time.sleep(time_sleep)
                    self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click() #Go Back 1 Page
                    time.sleep(time_sleep)
                except Exception as e :
                    print(e)
                    back = False
                    print("Finish accept friend request.")

            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click() #Go Back 1 Page
            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
            time.sleep(time_sleep)

        except Exception as e :
            print(e)
            print("You are not start at home page.")

        self.driver.quit()

M=Moments()
M.main()
