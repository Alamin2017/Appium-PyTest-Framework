import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

desired_cap = {
    "app": "D:\Soft\Android_Studio\Android_Demo_App.apk",
    "platformName": "Android",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                          'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'))

"""actions = TouchAction(driver)
actions.long_press(ele,5)
actions.perform()"""

action = ActionChains(driver)
action.click_and_hold(ele).perform()

time.sleep(4)
driver.quit()
