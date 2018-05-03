import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from InstasizePages import EditorPage


def _by_link_text():
    pass


class CameraTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        gridPage    = GridPage(driver)
        editorPage  = EditorPage(driver)
        tryExcepts  = TryExcepts(driver)

        gridPage.skip_onboarding()

        gridPage.purchasPremiumEditor()

        gridPage.addPhotoTap()

        # Asserts collapseIcon is displayed
        gridPage.assertCollapseIconPresent()

        # taps on the camera icon
        gridPage.tap_camera_icon()

        # takes a picture
        gridPage.take_photo()

        # taps on ok
        gridPage.tap_camera_ok()

        # taps on share button
        editorPage.tapSharebutton()

        gridPage.tapInstagramIcon()

        # Searches for Instagram android popup on bottom of screen
        tryExcepts.instagramSystemPopup()

        sleep(5)

        # Asserts the + button is displayed
        gridPage.addPhotoFind()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CameraTest)
    unittest.TextTestRunner(verbosity=2).run(suite)