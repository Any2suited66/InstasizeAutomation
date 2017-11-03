import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep




def _by_link_text():
    pass


class TestReviewPopupTest(unittest.TestCase):

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

        # taps photo on grid page
        tapGridPhoto = GridPage(driver)
        tapGridPhoto.topLeftPhotoGridtap()

        # taps the delete button on grid page
        deleteButtonTap = GridPage(driver)
        deleteButtonTap.deleteButtontTap()

        # asserts setting icon is visible
        settingsIcon = GridPageAsserts(driver)
        settingsIcon.settingsIconAssert()

        driver.quit()
        sleep(3)


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReviewPopupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)