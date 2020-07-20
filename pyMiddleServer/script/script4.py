import time
import sys
import random
from appium import webdriver


deviceName = sys.argv[1]
serverSerial = int(deviceName.split(':', 1)[0].split('.')[3])
systemPort = str(serverSerial * 100 + 5)
wdaLocalPort = str(serverSerial * 100 + 10)
# webdriverURL = 'http://localhost:2472' + str(serverSerial % 10) + '/wd/hub'
# webdriverURL = 'http://localhost:2472' + str(random.randint(1, 9)) + '/wd/hub'
webdriverURL = 'http://localhost:24723/wd/hub'

print('systemPort: %s, wdaLocalPort: %s, deviceName: %s, serverSerial: %s' %
      (systemPort, wdaLocalPort, deviceName, serverSerial))
# print('webdriverURL: %s' % (webdriverURL))

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

time.sleep(random.randint(1, 6))
tStart = time.time()

driver = webdriver.Remote(webdriverURL, desired_caps)
driver.implicitly_wait(3)

initCost = time.time() - tStart
workCost = 0.0
try:
    tStart = time.time()
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
    workCost = time.time() - tStart
except Exception as e:
    print("Something wrong")
    print(e)

time.sleep(3)
driver.quit()
print("# %s init cost %f sec(s), work cost %f sec(s)" %
      (serverSerial, initCost, workCost))
