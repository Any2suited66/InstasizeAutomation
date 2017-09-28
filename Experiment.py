import os
import unittest
from appium import webdriver
from time import sleep
from EditorPage import Filters
from GridPage import Grid
from SelectFormatPage import SelectFormat
from selenium.common.exceptions import NoSuchElementException

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
        driver = self.driver
        # taps on the + icon
        addPhoto = Grid(driver)
        addPhoto.addPhoto()
        collapseIcon = self.driver.find_element_by_id("ivCollapseIcon")
        self.assertTrue(collapseIcon.is_displayed(), "Failed, Check for Crash")
        sleep(3)
        # taps on the native photos container
        tapPhotoContainer = Grid(driver)
        tapPhotoContainer.photoContainers()
        sleep(3)
        allPhotosButton = self.driver.find_element_by_id("btnShowAlbumsList")
        self.assertTrue(allPhotosButton.is_displayed, "Failed, Check for Crash")
        # taps on the top left photo
        tapTopLeftPhoto = Grid(driver)
        tapTopLeftPhoto.topLeftPhoto()
        sleep(10)
        denyReview = Filters(driver).reviewPopup()
        try: denyReview.click()
        except NoSuchElementException:
            print('PlayStore review has been done')
        # taps on the filter
        filters = Filters(driver)
        filters.h1filter()
        tvFilterLevel = self.driver.find_element_by_id("tvFilterLevel")
        self.assertTrue(tvFilterLevel.is_displayed, "Failed, Check for Crash")
        sleep(10)
        # taps on share button
        tapShareButton = Filters(driver)
        tapShareButton.sharebutton()
        sleep(7)
        # Taps on instagram icon
        tapInstagram = Grid(driver)
        tapInstagram.instagramIcon()
        sleep(10)
        instagramPopup = Grid(driver)
        try: instagramPopup.instagramPopup().click
        except NoSuchElementException:
            print('Does not exist on this version of android')
        # Searches for the + button
        uploadButton = Grid(driver).addPhoto()
        self.assertTrue(uploadButton.is_displayed(), "We have a problem!")


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeFilterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
