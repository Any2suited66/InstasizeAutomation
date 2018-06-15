import pytest
from appium import webdriver
from GetDeviceID import create_list_of_ids


class DriverBuilderAndroid(object):
    _multiprocess_can_split_ = True

    def __init__(self):
        self.setUp()

    @pytest.fixture()
    def setUp(self):
        getDeviceIDs = create_list_of_ids()
        print(getDeviceIDs)

        "Setup for the test"
        for x in getDeviceIDs:
            desired_caps = {}
            desired_caps['platformName'] = 'ANDROID'
            desired_caps['automationName'] = 'uiautomator2'
            desired_caps['deviceName'] = 'ANDROID'
            desired_caps['udid'] = ("%s" % x)
            # desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
            # desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20182704_release_4.0.14_131_google.apk'
            desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
            desired_caps['appPackage'] = 'com.jsdev.instasize'
            # desired_caps['noReset'] = True
            desired_caps['newCommandTimeout'] = 999999
            self.driver = webdriver.Remote('http://192.168.99.1:4444/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()