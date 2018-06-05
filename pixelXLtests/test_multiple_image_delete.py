import unittest
from pixelXLtests.pixelXLDriverBuilder import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class TestDeletePhoto(unittest.TestCase):

    def testDelete(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        gridPage = GridPage(driver)
        editorPage = EditorPage(driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()
        filterExportHelper.setupFilter()

        # taps on share icon
        editorPage.tapSharebutton()

        sleep(2)
        driver.back()

        filterExportHelper.setupFilter()

        # taps on share icon
        tapShareButton = EditorPage(driver)
        tapShareButton.tapSharebutton()

        sleep(2)
        driver.back()

        # Taps on the top left image on the grid
        gridPage.tapTopLeftPhotoOnGrid()

        # taps on the second image on grid screen
        gridPage.tap_second_grid_image()

        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()

        # Taps on cancel
        gridPage.tapCancelButton()

        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()

        # Taps on delete button in popup
        gridPage.tapDeleteButton()

        # Asserts the image was deleted successfully
        assertsImageDeleted = GridPageAsserts(driver)
        assertsImageDeleted.gridPagePhotoNotPresent()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeletePhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
