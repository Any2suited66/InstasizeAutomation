import unittest

from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from InstasizePages import EditorPage
from InstasizePages import CollagePage
from PaidFiltersPage import PaidEditorPage


def _by_link_text():
    pass


class CollageFilter1imgExportTest(unittest.TestCase):
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
        tapCollageContainer = GridPage(driver)
        tapCollageContainer.collageButtonTap()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tapTopLeftPhoto = CollagePage(driver)
        tapTopLeftPhoto.topLeftPhoto()

        # taps on the next photo to the right
        tapOnNextPhoto = CollagePage(driver)
        tapOnNextPhoto.tap2ndPhoto()

        # taps on the 3rd photo
        tapOnPhoto = CollagePage(driver)
        tapOnPhoto.tap3rdPhoto()

        # taps on 5th collage option to open editor
        tapOnCollageOption = CollagePage(driver)
        tapOnCollageOption.tap5thCollageOption()

        # taps on the filter
        filters = PaidEditorPage(driver)
        filters.aryaFilter()

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

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CollageFilter1imgExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)