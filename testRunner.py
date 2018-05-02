import os
import unittest
import pytest
from appium import webdriver
from test_SingleImageFilterExport import FilterExportTest
from test_Adjustments import AdjustmentsTest
from test_Crop import Crop_Feature
from test_CollageFilterExport import CollageExportTest
from test_BorderFeature import BordersFeatureTest
from test_NonHDFilterExport import NonHDFilterExportTest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.mark.userfixtures('setUp')
class InstasizeTests(unittest.TestCase):

    # @pytest.fixture()
    # def setUp(self):
    #     # getDevice = GetDeviceID()
    #     "Setup for the test"
    #
    #     desired_caps = {}
    #     desired_caps['platformName'] = 'ANDROID'
    #     desired_caps['automationName'] = 'uiautomator2'
    #     desired_caps['deviceName'] = 'ANDROID'
    #     desired_caps['udid'] = '8802edf5'
    #     # desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
    #     desired_caps['app'] = '/Users/tyler/Desktop/appium-docker-android-master/Appium/InstasizeInstallAPK/Instasize_20180903_release_4.0.11_128_google.apk'
    #     desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
    #     desired_caps['appPackage'] = 'com.jsdev.instasize'
    #     # desired_caps['noReset'] = True
    #     desired_caps['newCommandTimeout'] = 999999
    #     url = 'http://localhost:4723/wd/hub'
    #     self.driver = webdriver.Remote(url, desired_caps)

    # def teardown(self):
    #     self.driver.quit()


    def runFilterExportTest(self):
        FilterExportTest.test_filter_uploads(FilterExportTest)

    def runAdjustmentsTest(self):
        AdjustmentsTest.test_allAdjustments(AdjustmentsTest)

    def runCropFeatureTest(self):
        Crop_Feature.test_crop(Crop_Feature)

    def runCollageTest(self):
        CollageExportTest.test_collage_filter_uploads(CollageExportTest)

    def runBorderTest(self):
        BordersFeatureTest.test_borders(BordersFeatureTest)

    def runNonHDFilterTest(self):
        NonHDFilterExportTest.test_filter_uploads(NonHDFilterExportTest)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InstasizeTests)
    unittest.TextTestRunner(verbosity=2).run(suite)