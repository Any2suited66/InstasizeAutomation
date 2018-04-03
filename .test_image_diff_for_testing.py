from subprocess import run
from skimage.measure import compare_ssim
import cv2
import unittest
from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from InstasizePages import GridPage, EditorPage
from time import sleep

def _by_link_text():
    pass


class ImageComparisonTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tap2ndPhoto = GridPage(driver)
        tap2ndPhoto.second_grid_image()

        # taps on the filter
        filters = EditorPage(driver)
        filters.bDayFilter()

        # taps on date spinner
        bDaySpinner = EditorPage(driver)
        bDaySpinner.tapBdayDateSpinner()

        # swipes down on the date spinner
        tapOn1999 = EditorPage(driver)
        tapOn1999.tapBdaySpinnerForInput()

        # taps on create my filter button
        tapOnCreateMyFilter = EditorPage(driver)
        tapOnCreateMyFilter.tapCreateMyFilter()

        # taps on Use Filter
        tapUseFilter = EditorPage(driver)
        tapUseFilter.tapUseFilter()

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(driver)
        tvFilterLevel.tvFilterLevel()

        # takes a screenshot and pulls it to a specific folder
        sleep(10)
        run('adb shell screencap -p /sdcard/screencap.png', shell=True)
        sleep(10)
        run("adb pull /sdcard/screencap.png /Users/tyler/Desktop/imageComparisonFiles", shell=True)

        sleep(10)

        # loads the two input images
        imageA = cv2.imread('/Users/tyler/Desktop/imageComparisonFiles/s6BirthdayScreenshot.png')
        imageB = cv2.imread('/Users/tyler/Desktop/imageComparisonFiles/screencap.png')

        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        SSIM = ("SSIM: {}".format(score))
        print(SSIM)

        if ("{}".format(score)) <= '.80':
            print('SSIM is too low, please test manually', 'FAILED')

        else:
            print('SSIM is within acceptable range')

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ImageComparisonTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

