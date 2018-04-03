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


class AdjustmentsFeatureTest(unittest.TestCase):
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
        tapTopLeftPhoto.tapTopLeftPhoto()

        # taps the settings feature
        tapAdjustments = EditorPage(driver)
        tapAdjustments.tapAdjustmentsFeature()

        # taps adjustment
        tapAdjustment = EditorPage(driver)
        tapAdjustment.tapSharpness()

        # adjusts the seek bar
        adjustSeek = EditorPage(driver)
        adjustSeek.adjustSeekBar()

        # taps the accept Button
        tapAccept = EditorPage(driver)
        tapAccept.tapAccept()

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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AdjustmentsFeatureTest)
    unittest.TextTestRunner(verbosity=2).run(suite)