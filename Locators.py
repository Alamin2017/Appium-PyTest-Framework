from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_cap = {
    "app": "D:\Soft\Android_Studio\Android_Demo_App.apk",
    "platformName": "Android",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
#explicit wait concept
#wait = WebDriverWait(driver, 25, poll_frequency=1,
#                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
#                                         NoSuchElementException])
#ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("Views")'))
#ele.click()

# use index element finding
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(11)").click()

# use text for element finding
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Views")').click()

# use content desc for element finding
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("Views")').click()
print(driver.current_package)
