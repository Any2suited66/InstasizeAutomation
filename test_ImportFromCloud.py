import unittest
from time import sleep
from Asserts import GridPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from ExportHelper import FilterExportHelper

def _by_link_text():
    pass


class ImportFromCloud(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver
        gridPage = GridPage(driver)
        gridPageAsserts = GridPageAsserts(driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()
        gridPage.purchasPremiumEditor()

        # taps on the + icon
        gridPage.addPhotoTap()

        # taps on cloud option
        gridPage.tapOnCloudOption()

        # taps on the second image
        gridPage.tapOnCloudImageInSystem()

        filterExportHelper.filterExportInstagram()

        sleep(5)
        driver.back()
        gridPageAsserts.settingsIconAssert()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ImportFromCloud)
    unittest.TextTestRunner(verbosity=2).run(suite)