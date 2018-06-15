import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class TestDeletePhoto(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        editorPage = EditorPage(driver)
        gridPage = GridPage(driver)
        gridPageAsserts = GridPageAsserts(driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()
        filterExportHelper.setupFilter()

        editorPage.tapSharebutton()

        sleep(5)
        driver.back()

        # Taps on the top left image on the grid
        gridPage.tapTopLeftPhotoOnGrid()

        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()

        # Taps on cancel
        gridPage.tapCancelButton()

        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()

        # Taps on delete button in popup
        gridPage.tapDeleteButton()

        # Asserts the image was deleted successfully
        gridPageAsserts.gridPagePhotoNotPresent()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeletePhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
