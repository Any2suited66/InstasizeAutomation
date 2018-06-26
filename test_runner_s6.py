
import unittest
from appium import webdriver
from Base_tests import BaseTests


class TestRunnerS6(unittest.TestSuite):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = '05157df532e5e40e'
        desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20182704_release_4.0.14_131_google.apk'
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 999999
        desired_caps['systemPort'] = 7779
        self.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)

    def test_bday_filter(self):
        BaseTests(self).bday_filter_test()

    def test_adjustments(self):
        base_test = BaseTests(self.driver)
        base_test.adjustments_feature_test()

    def test_announcements(self):
        base_test = BaseTests(self.driver)
        base_test.whats_new_test()

    def test_border_feature(self):
        base_test = BaseTests(self.driver)
        base_test.border_feature_test()

    def test_camera_image(self):
        base_test = BaseTests(self.driver)
        base_test.camera_test()

    def test_collage_feature(self):
        base_test = BaseTests(self.driver)
        base_test.collage_test()

    def test_create_profile(self):
        base_test = BaseTests(self.driver)
        base_test.create_new_profile_test()

    def test_crop_feature(self):
        base_test = BaseTests(self.driver)
        base_test.crop_feature_test()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRunnerS6)
    unittest.TextTestRunner(verbosity=2).run(suite)
