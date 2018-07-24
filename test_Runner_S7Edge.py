import unittest
from appium import webdriver
from Base_tests import BaseTests
import APKInstall


class TestRunnerS7(unittest.TestCase):

    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = '8802edf5'
        desired_caps['platformVersion'] = '7.0'
        # desired_caps['app'] = APKInstall.install_APK()
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 999999
        desired_caps['systemPort'] = 7785
        desired_caps['autoGrantPermissions'] = True
        desired_caps['autoDismissAlerts'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4450/wd/hub', desired_caps)

    def test_bday_filter(self):
        BaseTests(self.driver).bday_filter_test()

    def test_adjustments(self):
        BaseTests(self.driver).adjustments_feature_test()

    def test_announcements(self):
        BaseTests(self.driver).whats_new_test()

    def test_border_feature(self):
        BaseTests(self.driver).border_feature_test()

    def test_camera_image(self):
        BaseTests(self.driver).camera_test()

    def test_collage_feature(self):
        BaseTests(self.driver).collage_test()

    def test_create_profile(self):
        BaseTests(self.driver).create_new_profile_test()

    def test_crop_feature(self):
        BaseTests(self.driver).crop_feature_test()

    def test_delete_image(self):
        BaseTests(self.driver).delete_image()

    def test_import_cloud_image(self):
        BaseTests(self.driver).import_from_cloud()

    def test_instasize_btn(self):
        BaseTests(self.driver).instasize_btn_test()

    def test_login_to_profile(self):
        BaseTests(self.driver).login_to_profile()

    def test_delete_multiple_images(self):
        BaseTests(self.driver).delete_multiple_images()

    def test_non_hd_filter_test(self):
        BaseTests(self.driver).non_hd_filter_export()

    def test_single_image_export(self):
        BaseTests(self.driver).single_image_export_test()

    def test_tools(self):
        BaseTests(self.driver).tools_test()

    def test_social_media_icons(self):
        BaseTests(self.driver).test_social_media_icons()

    def test_send_feedback(self):
        BaseTests(self.driver).test_send_feedback_in_settings()

    def test_write_a_review_in_settings(self):
        BaseTests(self.driver).test_write_a_review_in_settings()

    def test_terms_conditions_in_settings(self):
        BaseTests(self.driver).test_terms_and_conditions()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRunnerS7)
    unittest.TextTestRunner(verbosity=2).run(suite)