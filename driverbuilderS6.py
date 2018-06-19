import pytest
from appium import webdriver



class DriverBuilderAndroidS6(object):
    _multiprocess_can_split_ = True

    def __init__(self):
        self.setUp_S7()


    @pytest.fixture()
    def setUp_S7(self):
        # getDevice = GetDeviceID()
        "Setup for the test"


        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = '05157df532e5e40e'
        desired_caps['platformVersion'] = '7.0'
        # desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20182704_release_4.0.14_131_google.apk'
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 999999
        desired_caps['systemPort'] = '7779'
        self.driver = webdriver.Remote('http://127.0.0.1:4400/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()