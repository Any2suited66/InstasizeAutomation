import unittest

from Asserts import PhotoLibraryAsserts, EditorPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from PaidFiltersPage import PaidEditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from InstasizePages import EditorPage


def _by_link_text():
    pass


class PurchasesTest(unittest.TestCase):
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

        # taps on the filter
        filters = PaidEditorPage(driver)
        filters.freeH1Filter()

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(driver)
        tvFilterLevel.tvFilterLevel()

        # Taps on premium banner
        premium_banner = EditorPage(driver)
        premium_banner.tapPremiumBanner()

        # Asserts premium page is opened from editor
        premium_coodinator = EditorPageAsserts(driver)
        premium_coodinator.premiumPageAssert()

        # Asserts the share button is not shown
        shareButtonNotShown = EditorPageAsserts(driver)
        shareButtonNotShown.shareButtonNotDisplayed()

        # Taps on 'Yes, Discard'
        tapConfirmDiscard = EditorPage(driver)
        tapConfirmDiscard.discardEditsConfirm()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PurchasesTest)
    unittest.TextTestRunner(verbosity=2).run(suite)