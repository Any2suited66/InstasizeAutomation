import unittest
from s6Tests.s6DriverBuilder import DriverBuilderAndroid
from InstasizePages import GridPage
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

        sleep(5)

        driver.back()

        # Asserts the + button is displayed
        gridPage.addPhotoFind()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CameraTest)
    unittest.TextTestRunner(verbosity=2).run(suite)