import unittest
from time import sleep
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from ExportHelper import FilterExportHelper
def _by_link_text():
    pass


class InstasizeButtonExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_export(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        gridPage = GridPage(driver)
        editorPage = EditorPage(driver)
        filterExportHelper = FilterExportHelper()

        filterExportHelper.setupFilter()

        # taps on the yellow instasize button
        editorPage.tapInstasizeButton()

        filterExportHelper.filterExportInstagram()

        # Asserts the + button is displayed
        gridPage.addPhotoFind()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeButtonExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)