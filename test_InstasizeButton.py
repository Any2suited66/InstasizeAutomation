import unittest
from time import sleep

from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts


def _by_link_text():
    pass


class InstasizeButtonExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_export(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.assertCollapseIconPresent()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.tapPhotoContainer()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.tapTopLeftImageInPhotoLibrary()

        # taps on the yellow instasize button
        tapInstasizeButton = EditorPage(driver)
        tapInstasizeButton.tapInstasizeButton()

        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.tapSharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.tapInstagramIcon()

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
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeButtonExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)