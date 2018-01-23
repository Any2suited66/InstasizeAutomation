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
        desired_caps['deviceName'] = 'null'
        desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20180501_release_4.0.8b2_126_google.apk'
        desired_caps['appPackage'] = 'com.jsdev.instasize'

        self.driver = webdriver.Remote('http://0.0.0.0:4444/wd/hub', desired_caps)
        # desired_caps['port'] = os.environ['PORT'] if "PORT" in os.environ else 4723
        # desired_caps['deviceName'] = os.environ['UDID'] if "UDID" in os.environ else getDevice.getDeviceID()
        # Returns abs path relative to this file and not cwd


        # desired_caps['appActivity'] = '.activities.MainActivity'






    def tearDown(self):
        self.driver.quit()
