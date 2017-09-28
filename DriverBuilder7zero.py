import os
import unittest

from appium import webdriver
from time import sleep


def _by_link_text():
    pass


class DriverBuilder(unittest.TestCase):
    "Class to run tests on Instasize on android 7.0"

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