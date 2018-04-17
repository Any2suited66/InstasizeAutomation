from time import sleep

from selenium.common.exceptions import NoSuchElementException

from ExportHelper import FilterExportHelper
from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts


class AdjustmentsHelper(object):
    def __init__(self, driver):
        self.driver = driver

    def allAdjustments(self):
        adjustmentsList = ["//android.widget.TextView[@text ='CONTRAST']", "//android.widget.TextView[@text ='EXPOSURE']",
                           "//android.widget.TextView[@text ='BRIGHTNESS']", "//android.widget.TextView[@text ='SHARPNESS']",
                           "//android.widget.TextView[@text ='SATURATION']", "//android.widget.TextView[@text ='TINT']",
                           "//android.widget.TextView[@text ='WARMTH']", "//android.widget.TextView[@text ='VIGNETTE']",
                           "//android.widget.TextView[@text ='SHADOWS']", "//android.widget.TextView[@text ='HIGHLIGHTS']",
                           "//android.widget.TextView[@text ='GRAIN']"]

        filterExportHelper = FilterExportHelper()

        editorPage = EditorPage(self.driver)
        filterExportHelper.setupFilter()
        editorPage.tapAdjustmentsFeature()

        for a in adjustmentsList:
            for x in range(0, 11):
                try:
                    adjustment = self.driver.find_element_by_xpath("(""%s"")" % a)
                    sleep(2)
                    adjustment.click()
                    editorPage.adjustSeekBar()
                    editorPage.tapAccept()
                    break

                except NoSuchElementException:
                    editorPage.swipeInEditor()

        editorPage.tapSharebutton()

        # Taps on Instagram icon
        gridPage = GridPage(self.driver)
        gridPage.tapInstagramIcon()

        # Searches for Instagram android popup on bottom of screen
        tryExceots = TryExcepts(self.driver)
        tryExceots.instagramSystemPopup()

        sleep(5)
        self.driver.back()
