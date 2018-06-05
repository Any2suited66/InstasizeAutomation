import unittest
from time import sleep

from Asserts import GridPageAsserts
from pixelXLtests import pixelXLDriverBuilder
from InstasizePages import GridPage


def _by_link_text():
    pass


class TestAnnouncements(unittest.TestCase):

    driverBuilder = pixelXLDriverBuilder.DriverBuilderAndroid()
    driver = driverBuilder.driver

    def runTest(self):

        gridPage = GridPage(self.driver)

        gridPage.skip_onboarding()

        gridPage.tapWhatsNewBtn()

        sleep(5)
        self.driver.back()

    def plus_icon_assert(self):
        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.settingsIconAssert()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnnouncements)
    unittest.TextTestRunner(verbosity=2).run(suite)