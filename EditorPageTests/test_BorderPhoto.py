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


class BordersFeatureTest(unittest.TestCase):
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

        # taps on the top left photo
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()

        # taps on the borders feature
        tapBorders = EditorPage(driver)
        tapBorders.tapBorderFeature()

        # taps on the border pack
        tapBorderPack = EditorPage(driver)
        tapBorderPack.tapPhotoBorder()

        # taps blur option
        tapBlur = EditorPage(driver)
        tapBlur.tapBlurPhotoBorder()

        # taps on the top left image in photo library
        tapTopLeftPhoto.topLeftPhoto()

        # taps accept
        tapAccept = EditorPage(driver)
        tapAccept.tapAccept()

        # taps share button
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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BordersFeatureTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
