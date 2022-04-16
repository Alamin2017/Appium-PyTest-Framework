from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = ('D:\Soft\Android_Studio\Android_Demo_App.apk')
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

