import os
from appium import webdriver
from GetDeviceID import GetDeviceID
import GetAndroidVersion
import APKInstall



class DriverBuilderAndroid(object):
    _multiprocess_can_split_ = True

    def __init__(self):
        self.setUp()

    def setUp(self):
        # getDevice = GetDeviceID()
        "Setup for the test"

        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = '05157df532e5e40e'
        # desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        desired_caps['app'] = '/Users/tyler/Desktop/appium-docker-android-master/Appium/InstasizeInstallAPK/Instasize_20180903_release_4.0.11_128_google.apk'
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
