import os
import unittest
from appium import webdriver
from time import sleep
from InstasizePages import EditorPage
from InstasizePages import GridPage
from InstasizePages import PhotoLibraryPage
from Asserts import PhotoLibraryAsserts
from selenium.common.exceptions import NoSuchElementException
from DriverBuilder7zero import DriverBuilderAndroid


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

     def test_filter_uploads(self):
        sleep(4)
        driver = self.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()
        sleep(3)

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()
        sleep(3)

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()
        sleep(10)

        # Searches for the Review Popup and dismisses it
        try:
            self.driver.find_element_by_id("btnDeny").click()
        except NoSuchElementException:
            print('PlayStore review popup did not occur')

        # taps on the filter
        filters = EditorPage(driver)
        filters.h1filter()

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(driver)
        tvFilterLevel.tvFilterLevel()


        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()
        sleep(7)

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.instagramIcon()
        sleep(10)

        # Searches for Instagram android popup on bottom of screen
        try:
            self.driver.find_element_by_id("icon").click()
        except NoSuchElementException:
            print("Not required on this version of android")
        sleep(5)
        self.driver.back()
        sleep(5)

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeFilterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
