import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage, ProfilePage
from Asserts import GridPageAsserts
from time import sleep



def _by_link_text():
    pass


class TestProfileLogin(unittest.TestCase):
    driverBuilder = DriverBuilderAndroid()
    driver = driverBuilder.driver

    def test_runTest(self):
        gridPage = GridPage(self.driver)
        profilePage = ProfilePage(self.driver)

        gridPage.skip_onboarding()
        profilePage.openProfilePage()
        profilePage.tapSignIn()
        profilePage.enterLoginInfo()
        profilePage.tapSignUp()

    def test_settings_icon_asser(self):
        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.settingsIconAssert()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProfileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)