import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep
from PaidFiltersPage import PaidEditorPage
from TryExcepts import TryExcepts

def _by_link_text():
    pass


class ImportFromCloud(unittest.TestCase):

    def runTest(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # taps on cloud option
        tapOnCloud = GridPage(driver)
        tapOnCloud.tapOnCloudOption()

        # taps on the second image
        tapOnImage = GridPage(driver)
        tapOnImage.tapOnCloudImage()

        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.instagramIcon()

        # Searches for Instagram android popup on bottom of screen
        instagramSystemPopup = TryExcepts(driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(2)
        driver.back()

        assertSettingsIcon = GridPageAsserts(driver)
        assertSettingsIcon.settingsIconAssert()

        sleep(2)
        driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ImportFromCloud)
    unittest.TextTestRunner(verbosity=2).run(suite)