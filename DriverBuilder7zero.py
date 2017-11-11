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
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '8802edf5'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '/Users/tyler/Desktop/Instasize apk/Instasize_20170811_release_4.0.4_122_google.apk'))
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
