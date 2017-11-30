import os
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
        desired_caps['platformVersion'] = os.environ['PLATFORM_VERSION'] if "PLATFORM_VERSION" in os.environ else GetAndroidVersion.getVersion()
        port = os.environ['PORT'] if "PORT" in os.environ else 4723
        desired_caps['deviceName'] =  os.environ['UDID'] if "UDID" in os.environ else getDevice.getDeviceID()
        # Returns abs path relative to this file and not cwd

        desired_caps['app'] = APKInstall.installAPK()
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        port = os.environ['PORT'] if "PORT" in os.environ else 4723
        url = "http://localhost:%s/wd/hub" % port
        print url
        print desired_caps
        self.driver = webdriver.Remote(url, desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
