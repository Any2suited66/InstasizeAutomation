import unittest
from time import sleep

from Asserts import GridPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage


def _by_link_text():
    pass


class TestAnnouncements(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver
        gridPage = GridPage(driver)
        gridPageAsserts = GridPageAsserts(driver)

        gridPage.tapWhatsNewBtn()

        sleep(2)
        driver.back()

        gridPageAsserts.settingsIconAssert()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnnouncements)
    unittest.TextTestRunner(verbosity=2).run(suite)