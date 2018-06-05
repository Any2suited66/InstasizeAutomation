import unittest
from s6Tests.s6DriverBuilder import DriverBuilderAndroid
from InstasizePages import GridPage
from time import sleep
from InstasizePages import EditorPage
from ExportHelper import FilterExportHelper

def _by_link_text():
    pass


class CropFeatureTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        gridPage = GridPage(driver)
        filterExportHelper = FilterExportHelper()
        editorPage = EditorPage(driver)


        filterExportHelper.setupFilter()

        # taps the tools feature
        editorPage.tapToolsFeature()

        # taps on all tool features
        editorPage.tapOnAllTools()

        filterExportHelper.filterExportInstagram()

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CropFeatureTest)
    unittest.TextTestRunner(verbosity=2).run(suite)