import unittest
from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep


def _by_link_text():
    pass


class NewportFilterExportTest(unittest.TestCase):
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

<<<<<<< HEAD:CoastFilterExport.py
=======
        # Searches for the Review Popup and dismisses it
        dismissReviewPopup = TryExcepts(driver)
        dismissReviewPopup.reviewPopup()

        swipeTwice = EditorPage(driver)
        swipeTwice.twoSwipesRtoL()

        # taps on the filter
        filters = EditorPage(driver)
        filters.newportFilter()

>>>>>>> origin/master:NewportFilterExport.py
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

        sleep(2)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

<<<<<<< HEAD:CoastFilterExport.py
        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()
=======
        sleep(5)
        driver.quit()
>>>>>>> origin/master:NewportFilterExport.py


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NewportFilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
