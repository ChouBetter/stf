from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PLATFORM='Android'
deviceName='HT44HWM06883'
app_package='com.tencent.mm'
app_activity='.ui.LauncherUI'
driver_server='http://127.0.0.1:4723/wd/hub'
noreset_flag='true'
fullreset_flag='false'



def main_menu():
    print("======================")
    print("1. Activate WeChat")
    print("2. Close WeChat")
    print("3. Open Moments")
    print("4. Open Broadcast Messages")
    print("5. Open profile")
    print("6. Open Nearby")
    print("7. Open Search")
    print("8. Clear Chats")
    print("9. Click Good")
    print("10. Auto post")
    print("11. Auto reply")
    print("12. group chat")
    print("13. Add friend into crrunt group")
    print("97. Tap test")
    print("98. Query app status")
    print("99. Exit")
    print("======================")

class Moments():
    def __init__(self):
        self.desired_caps={
        'platformName':PLATFORM,
        'deviceName':deviceName,
#       'appPackage':app_package,
#       'appActivity':app_activity,
        'noReset':noreset_flag,
        'fullReset':fullreset_flag}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,10)

    def login(self):
        print('login test ======')

    def enter(self):
        print('click find ======')
        self.wait=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/cdh"]/..'))) 
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

    def moments_test(self):
#        print('click test ======')
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Chats"]')))
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Discover"]')))
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
#        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Moments"]')))
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
#        time.sleep(3)
#        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kx"]').click()
#        self.driver.press_keycode(4)
#        time.sleep(3)
#        self.back_to_main_page()

    def broadcast_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Me"]')))
        self.driver.find_element_by_xpath('//*[@text="Me"]').click()
#        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Settings"]')))
        self.driver.find_element_by_xpath('//*[@text="Settings"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="General"]')))
        self.driver.find_element_by_xpath('//*[@text="General"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Plug-ins"]')))
        self.driver.find_element_by_xpath('//*[@text="Plug-ins"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Broadcast Messages"]')))
        self.driver.find_element_by_xpath('//*[@text="Broadcast Messages"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Send Now"]')))
        self.driver.find_element_by_xpath('//*[@text="Send Now"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="New Broadcast Message"]')))
        self.driver.find_element_by_xpath('//*[@text="New Broadcast Message"]').click()

    def me_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Me"]')))
        self.driver.find_element_by_xpath('//*[@text="Me"]').click()
#        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/qk"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/qk"]').click()

    def nearby_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Discover"]')))
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="People Nearby"]')))
        self.driver.find_element_by_xpath('//*[@text="People Nearby"]').click()
#        time.sleep(2)

    def contacts_test(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Contacts"]')))
        self.driver.find_element_by_xpath('//*[@text="Contacts"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@content-desc="More function buttons"]')))
        self.driver.find_element_by_xpath('//*[@content-desc="More function buttons"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Add Contacts"]')))
        self.driver.find_element_by_xpath('//*[@text="Add Contacts"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/d_4"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/d_4"]').click()

    def clean_chat_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Me"]')))
        self.driver.find_element_by_xpath('//*[@text="Me"]').click()
#        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Settings"]')))
        self.driver.find_element_by_xpath('//*[@text="Settings"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Chats"]')))
        self.driver.find_element_by_xpath('//*[@text="Chats"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Clear Chat History"]')))
        self.driver.find_element_by_xpath('//*[@text="Clear Chat History"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Clear"]')))
        self.driver.find_element_by_xpath('//*[@text="Clear"]').click()

    def launch_app_test(self):
#        print('launch app test ======')
        time.sleep(5)
        self.driver.activate_app('com.tencent.mm');

    def close_app_test(self):
#        print('close app test ======')
        time.sleep(5)
        self.driver.terminate_app('com.tencent.mm');
#        self.driver.close_app();

    def click_good_test(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Discover"]')))
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Moments"]')))
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
        time.sleep(3)
        self.driver.swipe(start_x=300, start_y=1000, end_x=300, end_y=800, duration=100)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/eho"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/eho"]').click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Like"]')))
        self.driver.find_element_by_xpath('//*[@text="Like"]').click()

    def auto_post_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Discover"]')))
        self.driver.find_element_by_xpath('//*[@text="Discover"]').click()
#        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Moments"]')))
        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/kj"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/kj"]').click()
#        time.sleep(3)
#        self.driver.find_element_by_xpath('//*[@text="Moments"]').click()
#        time.sleep(3)
#        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ekr"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Choose from Album"]')))
        self.driver.find_element_by_xpath('//*[@text="Choose from Album"]').click()
        time.sleep(3)
        self.driver.tap([(500,230)])
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/ki"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ki"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Say something..."]')))
        self.driver.find_element_by_xpath('//*[@text="Say something..."]').send_keys("Have a good vacation")
#        time.sleep(3)
#        self.driver.find_element_by_xpath('//*[@text="Post"]').click()
#        time.sleep(3)

    def auto_reply_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/nf"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/nf"]').click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/ami"]')))
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ami"]').send_keys("So good")

        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="Send"]')))
        self.driver.find_element_by_xpath('//*[@text="Send"]').click()

        self.driver.press_keycode(4)

    def group_chat_test(self):
    
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@content-desc="More function buttons"]')))
        self.driver.find_element_by_xpath('//*[@content-desc="More function buttons"]').click()
        
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="New Chat"]')))
        self.driver.find_element_by_xpath('//*[@text="New Chat"]').click()

        times=1
        for i in range(7,11):
            print('i = %s' % (i))
#            test = self.driver.find_element_by_xpath('//*[@checkable="true"]');
#            ccc = self.driver.find_element_by_xpath('//*[@class="android.widget.CheckBox"]').get_attribute('checked');
#            ccc = self.driver.find_element_by_xpath('//*[@class="android.widget.RelativeLayout"]');
            try:
                ccc = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index= %d ]" % (i) ).click();
            except:
                print("Some wrong")

        self.driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()


    def add_friend_into_group_test(self):
#        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@content-desc="Chat Info"]')))
        self.driver.find_element_by_xpath('//*[@content-desc="Chat Info"]').click()
#        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@content-desc="Add Members"]')))
        self.driver.find_element_by_xpath('//*[@content-desc="Add Members"]').click()
        time.sleep(3)
        for i in range(7,13):
            print('i = %s' % (i))
            try:
                ccc = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index= %d ]" % (i) ).click();
            except:
                print("Some wrong")
#        self.driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()


    def uiautomator_test(self):
#        print('query app test ======')
        time.sleep(5)
        result=self.driver.query_app_state('com.tencent.mm');
        print("result=%d" % result)

    def query_app_test(self):
#        print('query app test ======')
        time.sleep(5)
        result=self.driver.query_app_state('com.tencent.mm');
        print("result=%d" % (result))

    def tap_test(self):
        time.sleep(5)
#        self.driver.tap([(500,230)])
#        time.sleep(3)

    def back_to_main_page(self):
#        print('back test ======')
        try:
            chats=self.driver.find_element_by_xpath('//*[@text="Chats"]')
            print("chats = %s" % (chats))
        except:
            self.driver.press_keycode(4)
            print("Error")

    def main(self):
#        self.login()
#        self.enter()
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
                self.me_test()
            elif op == 6:
                self.nearby_test()
            elif op == 7:
                self.contacts_test()
            elif op == 8:
                self.clean_chat_test()
            elif op == 9:
                self.click_good_test()
            elif op == 10:
                self.auto_post_test()
            elif op == 11:
                self.auto_reply_test()
            elif op == 12:
                self.group_chat_test()
            elif op == 13:
                self.add_friend_into_group_test()
            elif op == 96:
                self.uiautomator_test()
            elif op == 97:
                self.tap_test()
            elif op == 98:
                self.query_app_test()
            elif op == 99:
                print("Exit")
                self.driver.quit()
                break
            else:
                print("No option")

M=Moments()
M.main()
