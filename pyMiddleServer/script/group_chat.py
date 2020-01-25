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

    def message_back_to_main(self):

        back = True
        while back is True :
            try :
                #print(self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]'))
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ls"]').click()
                time.sleep(3)
                back = True
            except Exception as e :
                print(e)
                back = False

        try :
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
            time.sleep(3)
        except Exception as e :
            print(e)

    def main(self):

        try : 
            num = int(input("Enter how many of members you want group chat: ")) # if enter 0 then select all friends

            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/rb"]').click() #click "+"
            time.sleep(time_sleep)
            self.driver.find_element_by_xpath('//*[@text="New Chat"]').click()
            time.sleep(time_sleep)
           
            # Select member to add group chat
            try:
                # list1 = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/a3j"]')[0].get_attribute('checked') 
                # print(list1) 
                # list2 = self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/a3j"]')[1].get_attribute('checked')
                # print(list2) 
                # time.sleep(time_sleep)

               
                for i in self.driver.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/a3j"]'):
                    # print(i.get_attribute('checked'))
                    if i.get_attribute('checked') == 'false':
                        i.click()
                        time.sleep(time_sleep)

                    if num == 1 :
                        break
                    elif num > 1 :
                        num = num-1
                    
            except Exception as e :
                print(e)
                print("Failure to group chat.")

            self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ln"]').click() #build group

            print("Finish build group chat.")

            self.message_back_to_main()

            # time.sleep(time_sleep)
            # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click() #Go Back 1 Page
            # time.sleep(time_sleep)
            # self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
            # time.sleep(time_sleep)

        except Exception as e :
            print(e)
            print("You are not start at home page.")

        self.driver.quit()

M=Moments()
M.main()
