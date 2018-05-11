import unittest
from InstasizePages import EditorPage
from InstasizePages import GridPage
from ExportHelper import FilterExportHelper
from DriverBuilder7zero import DriverBuilderAndroid
from time import sleep

class test_BirthdayFilterExport(unittest.TestCase):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_birthday_filter_export(self):

        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()
        gridPage.addPhotoTap()
        gridPage.tapPhotoContainer()
        gridPage.tapTopLeftImageInPhotoLibrary()
        editorPage.tapDenyReviewPopup()
        editorPage.tapBDayFilter()
        editorPage.tapBdayDateSpinner()
        editorPage.tapBdaySpinnerForInput()
        editorPage.tapCreateMyFilterBtn()
        editorPage.tapUseFilterBtn()
        filterExportHelper.filterExportInstagram()

        sleep(5)
        self.driver.back()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_BirthdayFilterExport)
    unittest.TextTestRunner(verbosity=2).run(suite)