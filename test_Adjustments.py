import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from AdjustmentsHelper import AdjustmentsHelper
from time import sleep
from ExportHelper import FilterExportHelper
from InstasizePages import EditorPage, GridPage
from TryExcepts import TryExcepts
from Asserts import GridPageAsserts
from selenium.common.exceptions import NoSuchElementException

def _by_link_text():
    pass


class AdjustmentsTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_allAdjustments(self):
        adjustmentsList = ["//android.widget.TextView[@text ='CONTRAST']", "//android.widget.TextView[@text ='EXPOSURE']",
                           "//android.widget.TextView[@text ='BRIGHTNESS']", "//android.widget.TextView[@text ='SHARPNESS']",
                           "//android.widget.TextView[@text ='SATURATION']", "//android.widget.TextView[@text ='TINT']",
                           "//android.widget.TextView[@text ='WARMTH']", "//android.widget.TextView[@text ='VIGNETTE']",
                           "//android.widget.TextView[@text ='SHADOWS']", "//android.widget.TextView[@text ='HIGHLIGHTS']",
                           "//android.widget.TextView[@text ='GRAIN']"]

        filterExportHelper = FilterExportHelper()
        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)

        gridPage.skip_onborading()
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

    def plus_icon_assert(self):
        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.settingsIconAssert()



# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AdjustmentsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
