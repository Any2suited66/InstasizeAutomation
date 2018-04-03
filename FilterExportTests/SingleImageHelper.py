import subprocess
import unittest
import appium
from appium import webdriver
from Asserts import PhotoLibraryAsserts
from DriverBuilder7zero import DriverBuilderAndroid
from PaidFiltersPage import PaidEditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from time import sleep
from InstasizePages import EditorPage
import json

def _by_link_text():
    pass





class SingleImageHelper:

    def __init__(self):
        self.setUP()

    def setUP(self):
        # getDevice = GetDeviceID()
        "Setup for the test"

        desired_caps = {}
        desired_caps['platformName'] = 'ANDROID'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'ANDROID'
        desired_caps['udid'] = '05157df532e5e40e'
        # desired_caps['platformVersion'] = GetAndroidVersion.getVersion()
        desired_caps[
            'app'] = '/Users/tyler/Desktop/appium-docker-android-master/Appium/InstasizeInstallAPK/Instasize_20180903_release_4.0.11_128_google.apk'
        desired_caps['appActivity'] = 'com.jsdev.instasize.activities.MainActivity'
        desired_caps['appPackage'] = 'com.jsdev.instasize'
        # desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def helper1thru5(self):

        # taps on the + icon
        gridPage = GridPage(self.driver)
        gridPage.addPhotoTap()

        # Asserts collapseIcon is displayed
        gridPage.collapseIconFind()

        # taps on the native photos container
        gridPage.photoContainers()

        # Asserts allPhotosButton is displayed
        photoLibraryAsserts = PhotoLibraryAsserts(self.driver)
        photoLibraryAsserts.allPhotosButton()

        # taps on the top left photo
        gridPage.tapTopLeftPhoto()

    def helper7thru11(self):

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(self.driver)
        tvFilterLevel.tvFilterLevel()

        # taps on share button
        tapShareButton = EditorPage(self.driver)
        tapShareButton.sharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(self.driver)
        tapInstagram.instagramIcon()

        # Searches for Instagram android popup on bottom of screen
        instagramSystemPopup = TryExcepts(self.driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(5)
        self.driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(self.driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(self.driver)
        quitTest.driverQuit()