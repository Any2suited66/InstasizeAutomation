import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import EditorPageAsserts
from time import sleep




def _by_link_text():
    pass


class TestReviewPopupTest(unittest.TestCase):
    _multiprocess_can_split_ = True

    # This method uninstalls the app off the test device to create the correct conditions
    def uninstallApp(self):
        driverBuildedr = DriverBuilderAndroid()
        driver = driverBuildedr.driver
        driver.remove_app()
        driver.quit()

    # Test for review popup in editor
    def test_ReviewPopup(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        addphoto = GridPage(driver)
        addphoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo on photo library page
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        sleep(2)
        driver.back()

        addphoto2 = GridPage(driver)
        addphoto2.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo on photo library page
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        sleep(2)
        driver.back()

        # taps photo on grid page
        tapGridPhoto = GridPage(driver)
        tapGridPhoto.topLeftPhotoGridtap()

        # taps on reedit button
        tapReeditButton = GridPage(driver)
        tapReeditButton.reeditButtontap()

        # asserts review popup is visible
        assertReviewPopup = EditorPageAsserts(driver)
        assertReviewPopup.giveAReview()

        # taps on 'Give A Review' button
        tapOnGiveReviewButton = EditorPage(driver)
        tapOnGiveReviewButton.giveAReviewButtonTap()

        sleep(2)
        driver.back()

        # asserts Instasize button is visible
        assertInstasizeButton = EditorPageAsserts(driver)
        assertInstasizeButton.instasizeButtonAssert()

        driver.quit()
        sleep(3)


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReviewPopupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
