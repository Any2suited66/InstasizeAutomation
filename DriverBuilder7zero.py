import os
from appium import webdriver


class DriverBuilderAndroid(object):

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'apps/InstaSize_R9_Test_3_7_6_107_collage_crash_fix_1.apk'))
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def __init__(self):
        self.driver, self.driverSetup()

    def teardown(self):
        self.driver.quit()

    def driverSetup(self):
        driverSetup = DriverBuilderAndroid()
        driverSetup.setUp()
