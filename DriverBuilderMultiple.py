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
        desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20180903_release_4.0.11_128_google.apk'

        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)



    def teardown(self):
        self.driver.quit()


