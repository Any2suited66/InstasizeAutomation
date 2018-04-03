import unittest

from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from PaidFiltersPage import PaidEditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from InstasizePages import EditorPage


def _by_link_text():
    pass


class FilterExportTest(unittest.TestCase):
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
        tapTopLeftPhoto.tapTopLeftPhoto()

        # taps on the filter
        filters = EditorPage(driver)
        filters.bDayFilter()

        # taps on date spinner
        bDaySpinner = EditorPage(driver)
        bDaySpinner.tapBdayDateSpinner()

        # swipes down on the date spinner
        tapOn1999 = EditorPage(driver)
        tapOn1999.tapBdaySpinnerForInput()

        # taps on create my filter button
        tapOnCreateMyFilter = EditorPage(driver)
        tapOnCreateMyFilter.tapCreateMyFilter()

        # taps on Use Filter
        tapUseFilter = EditorPage(driver)
        tapUseFilter.tapUseFilter()

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
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)