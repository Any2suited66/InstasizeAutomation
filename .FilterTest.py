import os
import unittest
from appium import webdriver
from time import sleep
import sys


def _by_link_text():
    pass


class InstasizeFilterTest(unittest.TestCase):
    "Class to run tests on exporting photos to Instagram"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '05157df532e5e40e'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '/Users/tyler/Desktop/Instasize_20172109_3.9.9_118_google.apk'))
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        desired_caps['appActivity'] = '.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_filter_uploads(self):
        sleep(4)
        # taps on the + icon
        element = self.driver.find_element_by_id("ibAddPhoto")
        element.click()
        sleep(3)
        # taps on the native photos container
        self.driver.find_element_by_id("photosContainer").click()
        sleep(3)
        #taps on the top left photo
        elmnt = self.driver.find_element_by_xpath("//android.widget.ImageView[@index=0]")
        elmnt.click()
        sleep(7)
        #taps on the filter
        elmnt = self.driver.find_element_by_xpath("//android.widget.ImageView[@index=1]")
        elmnt.click()
        sleep(3)
        #taps on share button
        elmnt = self.driver.find_element_by_xpath("//android.widget.ImageButton[@index=2]")
        elmnt.click()
        sleep(2)
        #Taps on instagram icon
        elmnt = self.driver.find_element_by_xpath("//android.widget.TextView[@index=1]")
        elmnt.click()
        sleep(10)
        self.driver.back()
        #Searches for the + button
        uploadButton = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
        self.assertTrue(uploadButton.is_displayed())


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeFilterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
