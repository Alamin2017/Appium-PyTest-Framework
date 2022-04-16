from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common import actions
from selenium.webdriver.support.wait import WebDriverWait
import time

desired_caps = {
    "app": "D:\Soft\Android_Studio\Android_Demo_App.apk",
    "platformName": "Android",
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))


TouchAction(driver).tap(x=524, y=1829).perform()

time.sleep(2)
driver.quit()
