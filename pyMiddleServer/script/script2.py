import time
import sys
import random
from appium import webdriver

deviceName = sys.argv[1]
serverSerial = int(deviceName.split(':', 1)[0].split('.')[3])
systemPort = str(serverSerial * 100 + 5)
wdaLocalPort = str(serverSerial * 100 + 10)
webdriverURL = 'http://localhost:2472' + str(random.randint(1, 9)) + '/wd/hub'

print('deviceName: %s, serverSerial: %s' % (deviceName, serverSerial))
print('systemPort: %s, wdaLocalPort: %s' % (systemPort, wdaLocalPort))
print('webdriverURL: %s' % (webdriverURL))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = deviceName
desired_caps['udid'] = deviceName
desired_caps['systemPort'] = systemPort
desired_caps['wdaLocalPort'] = wdaLocalPort

desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

desired_caps['noReset'] = 'true'
desired_caps['fullReset'] = 'false'

#driver = webdriver.Remote('http://123.51.133.103:24723/wd/hub', desired_caps)
#driver = webdriver.Remote('http://localhost:24723/wd/hub', desired_caps)
driver = webdriver.Remote(webdriverURL, desired_caps)

try:
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_9"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_8"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_7"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_6"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_5"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_4"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_3"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_1"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@resource-id="com.android.calculator2:id/digit_0"]').click()
    time.sleep(1)
except:
    print("Something wrong")

time.sleep(3)

driver.quit()
