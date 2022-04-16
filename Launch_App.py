from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

desired_cap = {
    "app": "D:\\Soft\\Android_Studio\\ApiDemos-debug.apk",
    "platformName": "Android",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Views']").click()
