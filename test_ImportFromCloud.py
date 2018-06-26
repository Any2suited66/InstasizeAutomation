import unittest
from time import sleep
from Asserts import GridPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage, EditorPage
from ExportHelper import FilterExportHelper

def _by_link_text():
    pass


class ImportFromCloud(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        self.driver = driverBuilder.driver
        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        filterExportHelper = FilterExportHelper()
        editor_page = EditorPage(self.driver)

        gridPage.purchasPremiumEditor()

        # taps on the + icon
        gridPage.addPhotoTap()

        # taps on cloud option
        gridPage.tapOnCloudOption()

        # taps on the second image
        gridPage.tapOnCloudImageInSystem()

        editor_page.purchase_premium_editor_popup()

        filterExportHelper.filterExportInstagram()

        gridPageAsserts.settingsIconAssert()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ImportFromCloud)
    unittest.TextTestRunner(verbosity=2).run(suite)