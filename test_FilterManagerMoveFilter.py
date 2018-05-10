import unittest
from time import sleep

from Asserts import PhotoLibraryAsserts, EditorPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class FilterManagerTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        editorPage = EditorPage(driver)
        gridPage = GridPage(driver)
        fitlerExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()

        fitlerExportHelper.setupFilter()

        # taps the filer manager
        editorPage.tapFilterManager()

        # moves the top filter down 3 spots
        editorPage.moveFilterInManager()

        # taps accept
        editorPage.tapAccept()

        fitlerExportHelper.filterExportInstagram()

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        gridPage.addPhotoFind()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterManagerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)