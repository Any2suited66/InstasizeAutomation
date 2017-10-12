import os
from appium import webdriver
from time import sleep

class DriverBuilderAndroid(object):

    def __init__(self):
        self.setUp()

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '/Users/tyler/Desktop/Instasize apk/InstaSize_R9_Test_3_7_6_107_collage_crash_fix_3.apk'))
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
