import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage, ProfilePage
from Asserts import GridPageAsserts
from time import sleep



def _by_link_text():
    pass


class TestProfileLogin(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        gridPage = GridPage(driver)
        gridPageAsserts = GridPageAsserts(driver)
        profilePage = ProfilePage(driver)

        gridPage.skip_onboarding()

        profilePage.openProfilePage()
        profilePage.tapSignIn()
        profilePage.enterLoginInfo()
        profilePage.tapSignUp()
        sleep(5)
        gridPageAsserts.settingsIconAssert()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProfileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)