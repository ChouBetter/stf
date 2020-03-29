#TikTok_try_registered
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys

PLATFORM='Android'
deviceName= sys.argv[1]#'G9AZCY0621977TH'#'ASUS_Z00LD'
app_package='com.ss.android.ugc.aweme'
app_activity='.main.MainActivity'
driver_server='http://123.51.133.103:24723/wd/hub'
#driver_server='http://127.0.0.1:4723/wd/hub'
noreset_flag='true'
fullreset_flag='false'

time_sleep = 3 # Delay Time

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

    def Try_registered(self):
        time.sleep(time_sleep)
        


    def main(self):
        while True:
            main_menu()
            op = int(input("Enter operation (1 - 99): "))
            if op < 1 or op > 99:
                print("Invalid operation: %d" % (op))
                time.sleep(2)

            if op == 1:
                self.Try_registered()

            elif op == 99:
                print("Exit")
                break
            else:
                print("No option")

M=Moments()
M.main()
