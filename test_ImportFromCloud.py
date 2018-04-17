import unittest
from time import sleep
from Asserts import GridPageAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts


def _by_link_text():
    pass


class ImportFromCloud(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver
        gridPage = GridPage(driver)
        editorPage = EditorPage(driver)
        tryExcepts = TryExcepts(driver)
        gridPageAsserts = GridPageAsserts(driver)
        # taps on the + icon
        gridPage.addPhotoTap()

        # taps on cloud option
        gridPage.tapOnCloudOption()

        # taps on the second image
        gridPage.tapOnCloudImageInSystem()

        # taps on share button
        editorPage.tapSharebutton()

        # Taps on Instagram icon
        gridPage.tapInstagramIcon()

        # Searches for Instagram android popup on bottom of screen
        tryExcepts.instagramSystemPopup()

        sleep(2)
        driver.back()
        gridPageAsserts.settingsIconAssert()

        sleep(2)
        driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ImportFromCloud)
    unittest.TextTestRunner(verbosity=2).run(suite)