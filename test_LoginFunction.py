import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import ProfilePage
from Asserts import GridPageAsserts
from time import sleep
from ExportHelper import FilterExportHelper



def _by_link_text():
    pass


class TestProfileLogin(unittest.TestCase):
    driverBuilder = DriverBuilderAndroid()
    driver = driverBuilder.driver

    def test_runTest(self):

        profilePage = ProfilePage(self.driver)
        filter_export_helper = FilterExportHelper()

        filter_export_helper.setupFilter()
        filter_export_helper.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.tapSignIn()
        profilePage.enterLoginInfo()
        profilePage.tapSignUp()


        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.settingsIconAssert()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProfileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)