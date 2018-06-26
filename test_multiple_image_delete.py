import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from Asserts import GridPageAsserts
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class TestDeletePhoto(unittest.TestCase):

    def testDelete(self):
        driverBuilder = DriverBuilderAndroid()
        self.driver = driverBuilder.driver

        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        filterExportHelper = FilterExportHelper()

        filterExportHelper.setupFilter()

        filterExportHelper.filterExportInstagram()

        filterExportHelper.setupFilter()

        filterExportHelper.filterExportInstagram()

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

        gridPageAsserts.settingsIconAssert()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeletePhoto)
    unittest.TextTestRunner(verbosity=2).run(suite)
