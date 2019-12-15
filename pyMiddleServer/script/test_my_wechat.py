from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys

PLATFORM='Android'
deviceName=sys.argv[1]#'G9AZCY0621977TH'#'ASUS_Z00LD'
app_package='com.tencent.mm'
app_activity='.ui.LauncherUI'
driver_server='http://123.51.133.103:24723/wd/hub'
# driver_server='http://127.0.0.1:4723/wd/hub'
noreset_flag='true'
fullreset_flag='false'

def main_menu():
    print("======================")
    print("1. Activate WeChat")
    print("2. Close WeChat")
    print("3. Open Moments")
    print("4. Open Broadcast Messages")
    print("5. Open profile")
    print("6. Open People Nearby")
    print("98. back to main")
    print("99. Exit")
    print("======================")

class Moments():
    def __init__(self):
        self.desired_caps={
        'platformName':PLATFORM,
        'deviceName':deviceName,
        'udid':deviceName,
        'appPackage':app_package,
        'appActivity':app_activity,
        'noReset':noreset_flag,
        'fullReset':fullreset_flag}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)

    def moments_test(self):
#        print('click test ======')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
        time.sleep(3)
#        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kx"]').click()
#        self.driver.press_keycode(4)
#        time.sleep(3)
#        self.back_to_main_page()

    def broadcast_test(self):
#        print('Broadcast test ======')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@text="Me"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="Settings"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="General"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="Plug-ins"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="Broadcast Messages"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="Send Now"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="New Broadcast Message"]').click()
        time.sleep(3)

    def open_my_profile(self):
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@text="Me"]').click()
        time.sleep(2)
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/dds"]')))
        tab.click()
        ##self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/qk"]').click()
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ddc"]').click()
        ## self.driver.find_element_by_id("com.tencent.mm:id/ddc").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
        time.sleep(3)

    def open_people_nearby(self):
        time.sleep(2)
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="Discover"]')))
        tab.click()
        #self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        time.sleep(2)
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@text="People Nearby"]')))
        print(type((By.XPATH,'//*[@text="People Nearby"]')))
        tab.click()
        #self.driver.find_element_by_xpath('//*[@text="People Nearby"]').click()

        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
        time.sleep(3)

    def back_to_main(self):

        back = True
        while back is True :
            try :
                #print(self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]'))
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/m0"]').click()
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

        print(self.driver.current_activity)

    def launch_app_test(self):
        time.sleep(5)
        self.driver.activate_app('com.tencent.mm');

    def close_app_test(self):
        time.sleep(5)
        self.driver.terminate_app('com.tencent.mm');
#        self.driver.close_app();


    def back_to_main_page(self):
        try:
            chats=self.driver.find_element_by_xpath('//*[@text="Chats"]')
            print("chats = %s" % (chats))
        except:
            self.driver.press_keycode(4)
            print("Error")

    def main(self):
        while True:
            main_menu()
            op = int(input("Enter operation (1 - 99): "))
            if op < 1 or op > 99:
                print("Invalid operation: %d" % (op))
                time.sleep(2)

            if op == 1:
                self.launch_app_test()
            elif op == 2:
                self.close_app_test()
            elif op == 3:
                self.moments_test()
            elif op == 4:
                self.broadcast_test()
            elif op == 5:
                self.open_my_profile()
            elif op == 6:
                self.open_people_nearby()
            elif op == 98:
                self.back_to_main()
            elif op == 99:
                print("Exit")
                break
            else:
                print("No option")

M=Moments()
M.main()
