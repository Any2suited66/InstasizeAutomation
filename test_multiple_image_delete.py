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

    def testDelete(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        addphoto = GridPage(driver)
        addphoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.assertCollapseIconPresent()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.tapPhotoContainer()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo on photo library page
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.tapTopLeftImageInPhotoLibrary()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.tapSharebutton()

        sleep(2)
        driver.back()

        addphoto = GridPage(driver)
        addphoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.assertCollapseIconPresent()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.tapPhotoContainer()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo on photo library page
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.tapTopLeftImageInPhotoLibrary()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.tapSharebutton()

        sleep(2)
        driver.back()

        # Taps on the top left image on the grid
        tapOnGridPhoto = GridPage(driver)
        tapOnGridPhoto.tapTopLeftPhotoOnGrid()

        # taps on the second image on grid screen
        tap2ndImage = GridPage(driver)
        tap2ndImage.second_grid_image()

        # Taps on delete icon
        tapDeleteIcon = GridPage(driver)
        tapDeleteIcon.tapDeleteIconOnGrid()

        # Taps on cancel
        tapOnCancel = GridPage(driver)
        tapOnCancel.tapCancelButton()

        # Taps on delete icon
        tapDeleteIcon.tapDeleteIconOnGrid()

        # Taps on delete button in popup
        tapDeleteButton = GridPage(driver)
        tapDeleteButton.tapDeleteButton()

        # Asserts the image was deleted successfully
        assertsImageDeleted = GridPageAsserts(driver)
        assertsImageDeleted.gridPagePhotoNotPresent()

        sleep(3)
        driver.quit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeletePhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
