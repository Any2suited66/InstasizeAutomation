import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage, ProfilePage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep
from PaidFiltersPage import PaidEditorPage


def _by_link_text():
    pass


class TestProfileLogin(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        profilePlusIcon = GridPage(driver)
        profilePlusIcon.openProfilePage()

        tapLogin = ProfilePage(driver)
        tapLogin.tapSignIn()

        enterLoginInfo = ProfilePage(driver)
        enterLoginInfo.enterLoginInfo()

        tapSignIn = ProfilePage(driver)
        tapSignIn.tapSignUp()

        assertSettingsIcon = GridPageAsserts(driver)
        assertSettingsIcon.settingsIconAssert()



        sleep(2)
        driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProfileLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)