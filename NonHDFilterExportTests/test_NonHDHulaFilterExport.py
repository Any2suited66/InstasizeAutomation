import unittest

from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from appium import webdriver

def _by_link_text():
    pass


class NonHDHulaFilterExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        # taps on the settings icon
        tapSettingsIcon = SettingsPage(driver)
        tapSettingsIcon.SettingsButton()

        # taps the hd switch
        tapHDSwitch = SettingsPage(driver)
        tapHDSwitch.HDExportButtonTap()

        driver.back()

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

        # taps on the filter
        filters = EditorPage(driver)
        filters.hulaFilter()

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
        instagramSystemPopup = TryExcepts(driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(3)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NonHDHulaFilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)