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

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.assertCollapseIconPresent()

        # taps on the camera icon
        tapCamera = GridPage(driver)
        tapCamera.tap_camera_icon()

        # takes a picture
        take_picture = GridPage(driver)
        take_picture.take_photo()

        # taps on ok
        tapCameraOkay = GridPage(driver)
        tapCameraOkay.tap_camera_ok()

        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.tapSharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.tapInstagramIcon()

        # Searches for Instagram android popup on bottom of screen
        instagramSystemPopup = TryExcepts(driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CameraTest)
    unittest.TextTestRunner(verbosity=2).run(suite)