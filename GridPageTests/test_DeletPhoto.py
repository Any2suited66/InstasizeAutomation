import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep


def _by_link_text():
    pass


class TestDeletePhoto(unittest.TestCase):

    def runTest(self):
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
        tapTopLeftPhoto.tapTopLeftPhoto()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        sleep(2)
        driver.back()

        # Taps on the top left image on the grid
        tapOnGridPhoto = GridPage(driver)
        tapOnGridPhoto.topLeftPhotoGridtap()

        # Taps on delete icon
        tapDeleteIcon = GridPage(driver)
        tapDeleteIcon.deleteIconTap()

        # Taps on cancel
        tapOnCancel = GridPage(driver)
        tapOnCancel.cancelButtonTap()

        # Taps on delete icon
        tapDeleteIcon.deleteIconTap()

        # Taps on delete button in popup
        tapDeleteButton = GridPage(driver)
        tapDeleteButton.deleteButtonTap()

        # Asserts the image was deleted successfully
        assertsImageDeleted = GridPageAsserts(driver)
        assertsImageDeleted.gridPagePhotoNotPresent()

        sleep(3)
        driver.quit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeletePhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
