from appium import webdriver

import time

desired_caps = {
    "automationName":"Appium",
    "platformName": "Android",
    "platformVersion":"11",
    "appPackage":"com.code2lead.kwad",
    "appActivity":"com.code2lead.kwad.MainActivity"

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(4)

driver.start_activity("com.facebook.katana","com.facebook.katana.LoginActivity")
time.sleep(10)
driver.quit()
