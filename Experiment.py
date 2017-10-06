import os
import unittest
from appium import webdriver
from time import sleep
from InstasizePages import EditorPage
from InstasizePages import GridPage
from Asserts import PhotoLibraryAsserts
from selenium.common.exceptions import NoSuchElementException
from DriverBuilder7zero import DriverBuilderAndroid


def _by_link_text():
    pass


class InstasizeFilterTest(unittest.TestCase):
     "Class to run tests on exporting photos to Instagram"

     def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()

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

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.instagramIcon()

        # Searches for Instagram android popup on bottom of screen
        try:
            self.driver.find_element_by_id("icon").click()
        except NoSuchElementException:
            print("Not required on this version of android")
        self.driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeFilterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
