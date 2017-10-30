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


class FluxFilterExportTest(unittest.TestCase):
     # Class to run tests on exporting photos to Instagram


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

<<<<<<< HEAD
=======
        # Searches for the Review Popup and dismisses it
        dismissReviewPopup = TryExcepts(driver)
        dismissReviewPopup.reviewPopup()

        # swipes 4 times to access filter
        swipe4times = EditorPage(driver)
        swipe4times.fourSwipesRtoL()

>>>>>>> origin/master
        # taps on the filter
        filters = EditorPage(driver)
        filters.fluxFilter()

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(driver)
        tvFilterLevel.tvFilterLevel()

<<<<<<< HEAD
=======

>>>>>>> origin/master
        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.instagramIcon()

        # Searches for Instagram android popup on bottom of screen
        instagramSystemPopup = TryExcepts(driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

<<<<<<< HEAD
        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()
=======
        sleep(10)
        driver.quit()
>>>>>>> origin/master


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FluxFilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)