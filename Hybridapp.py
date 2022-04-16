from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android',
                'appPackage': 'com.android.chrome',
                'appActivity': 'com.google.android.apps.chrome.Main'}

# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept"))
ele.click()

ele2 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button"))
ele2.click()

ele3 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
ele3.click()

ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
ele4.click()
ele4.send_keys("https://www.google.com/")

driver.press_keycode(66)

time.sleep(5)

appContexts = driver.contexts
print("AppContexts : ", appContexts)



