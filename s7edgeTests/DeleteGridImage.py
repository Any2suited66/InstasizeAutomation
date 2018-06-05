import unittest
from s7edgeTests.s7edgeDriverBuilder import DriverBuilderAndroid
from InstasizePages import GridPage
from InstasizePages import EditorPage
from Asserts import PhotoLibraryAsserts
from Asserts import GridPageAsserts
from time import sleep




def _by_link_text():
    pass


class TestReviewPopupTest(unittest.TestCase):


    # Test for review popup in editor
    def test_ReviewPopup(self):
        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        gridPage = GridPage(driver)
        editorPage = EditorPage(driver)
        gridPageAsserts = GridPageAsserts(driver)

        gridPage.skip_onboarding()
        gridPage.purchasPremiumEditor()
        gridPage.addPhotoTap()

        # taps on the native photos container
        gridPage.tapPhotoContainer()

        # taps on the top left photo on photo library page
        gridPage.tapTopLeftImageInPhotoLibrary()

        # taps on share icon
        editorPage.tapSharebutton()

        sleep(2)
        driver.back()

        # taps photo on grid page
        gridPage.tapTopLeftPhotoOnGrid()

        gridPage.tapDeleteIconOnGrid()

        # taps the delete button on grid page
        gridPage.tapDeleteButton()

        # asserts setting icon is visible
        gridPageAsserts.settingsIconAssert()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReviewPopupTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
