"""Do not use this file for testing.  This is used to experiment with different settings"""

from appium import webdriver
from GetDeviceID import GetDeviceID
import GetAndroidVersion
import APKInstall


class DriverBuilderAndroid(object):
    _multiprocess_can_split_ = True

    def __init__(self):
        self.setUp()

    def setUp(self):




        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'deviceName'
        desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        desired_caps['app'] = APKInstall.installAPK()

        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)



    def teardown(self):
        self.driver.quit()


