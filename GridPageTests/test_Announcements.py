import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep
from PaidFiltersPage import PaidEditorPage


def _by_link_text():
    pass


class TestAnnouncements(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        whatsNew = GridPage(driver)
        whatsNew.whatsNewBtnTap()

        sleep(2)
        driver.back()

        assertSettingsIcon = GridPageAsserts(driver)
        assertSettingsIcon.settingsIconAssert()

        sleep(2)
        driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnnouncements)
    unittest.TextTestRunner(verbosity=2).run(suite)