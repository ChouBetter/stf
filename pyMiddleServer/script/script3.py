import time
import sys
from appium import webdriver

print str(sys.argv[1])
deviceName = sys.argv[1]

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = deviceName
desired_caps['udid'] = deviceName

desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = 'false'

driver = webdriver.Remote('http://localhost:24723/wd/hub', desired_caps)

try:
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_9"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_8"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_7"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_6"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_5"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_4"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_3"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_1"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="com.android.calculator2:id/digit_0"]').click()
    time.sleep(1)
except:
    print("Something wrong")

time.sleep(3)

driver.quit()
