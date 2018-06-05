import pytest
from appium import webdriver



class DriverBuilderAndroid(object):
    _multiprocess_can_split_ = True

    def __init__(self):
        self.setUp()

    @pytest.fixture()
    def setUp(self):
        # getDevice = GetDeviceID()
        "Setup for the test"

        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = 'HT7160200777'
        # desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        # desired_caps['app'] = '/Users/tyler/Desktop/InstasizeInstallAPK/Instasize_20182704_release_4.0.14_131_google.apk'
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        desired_caps['chromedriverPort'] = '7070'
        desired_caps['systemPort'] = '7171'
        desired_caps['newCommandTimeout'] = 999999
        self.driver = webdriver.Remote('http://0.0.0.0:5678/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()