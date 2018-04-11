import unittest
from time import sleep
import inspect
from Asserts import PhotoLibraryAsserts
from InstasizePages import EditorPage, CollagePage
from InstasizePages import GridPage
from PaidFiltersPage import PaidEditorPage
from TryExcepts import TryExcepts
from DriverBuilder7zero import DriverBuilderAndroid
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
import inspect
import test_SingleImageFilterExport


class CropHelper(object):
    def __init__(self, driver):
        self.driver = driver

    def cropFeatures(self):


        cropFeatureList = ["//android.widget.TextView[@text ='FREE']", "//android.widget.TextView[@text ='1:1']",
                           "//android.widget.TextView[@text ='3:2']", "//android.widget.TextView[@text ='5:3']",
                           "//android.widget.TextView[@text ='4:3']", "//android.widget.TextView[@text ='5:4']",
                           "//android.widget.TextView[@text ='4:5']", "//android.widget.TextView[@text ='3:4']",
                           "//android.widget.TextView[@text ='2:3']", "//android.widget.TextView[@text ='7:5']",
                           "//android.widget.TextView[@text ='21:9']"]

        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)

        for a in cropFeatureList:
            gridPage.addPhotoTap()
            gridPage.photoContainers()
            gridPage.tapTopLeftPhoto()
            editorPage.reviewPopup()
            editorPage.tapCropFeature()
            for x in range(0, 10):
                try:
                    cropFeature = self.driver.find_element_by_xpath("(""%s"")" % a)
                    cropFeature.click()
                    editorPage.tapAccept()
                    editorPage.sharebutton()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editorPage.swipeInEditor()

            # Taps on Instagram icon
            gridPage = GridPage(self.driver)
            gridPage.instagramIcon()

            # Searches for Instagram android popup on bottom of screen
            tryExceots = TryExcepts(self.driver)
            tryExceots.instagramSystemPopup()

            sleep(5)
            self.driver.back()


