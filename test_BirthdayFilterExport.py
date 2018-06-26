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

        editorPage = EditorPage(self.driver)
        filterExportHelper = FilterExportHelper()

        version = self.driver.desired_capabilities['platformVersion']
        print(version)

        filterExportHelper.setupFilter()
        editorPage.tapBDayFilter()
        editorPage.tapBdayDateSpinner()
        editorPage.swipe_bday_spinner()
        # editorPage.tapBdaySpinnerForInput()
        editorPage.tapCreateMyFilterBtn()
        editorPage.tapUseFilterBtn()
        filterExportHelper.filterExportInstagram()

        sleep(5)
        self.driver.back()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_BirthdayFilterExport)
    unittest.TextTestRunner(verbosity=2).run(suite)