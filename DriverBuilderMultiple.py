"""Do not use this file for testing.  This is used to experiment with different settings"""

from appium import webdriver
from GetDeviceID import GetDeviceID
import GetAndroidVersion
import APKInstall

class DriverBuilderAndroid(object):

    def __init__(self):
        self.setUp()

    def setUp(self):
        getDevice = GetDeviceID()
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        desired_caps['deviceName'] = getDevice.getDeviceID()
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = APKInstall.installAPK()
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)






