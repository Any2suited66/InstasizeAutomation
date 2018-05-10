from time import sleep
from DriverBuilder7zero import DriverBuilderAndroid
from selenium.common.exceptions import NoSuchElementException
import unittest
from InstasizePages import EditorPage
from InstasizePages import GridPage

from ExportHelper import FilterExportHelper

class test_CropFeature(unittest.TestCase):


    def test_cropFeatures(self):

        driverBuilder = DriverBuilderAndroid()
        driver = driverBuilder.driver

        cropFeatureList = ["//android.widget.TextView[@text ='FREE']", "//android.widget.TextView[@text ='1:1']",
                           "//android.widget.TextView[@text ='3:2']", "//android.widget.TextView[@text ='5:3']",
                           "//android.widget.TextView[@text ='4:3']", "//android.widget.TextView[@text ='5:4']",
                           "//android.widget.TextView[@text ='4:5']", "//android.widget.TextView[@text ='3:4']",
                           "//android.widget.TextView[@text ='2:3']", "//android.widget.TextView[@text ='7:5']",
                           "//android.widget.TextView[@text ='21:9']"]


        gridPage = GridPage(driver)
        editorPage = EditorPage(driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()

        for a in cropFeatureList:
            filterExportHelper.setupFilter()
            editorPage.tapCropFeature()
            for x in range(0, 10):
                try:
                    cropFeature = driver.find_element_by_xpath("(""%s"")" % a)
                    cropFeature.click()
                    editorPage.tapAccept()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editorPage.swipeInEditor()

            filterExportHelper.filterExportInstagram()
            sleep(5)
            driver.back()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_CropFeature)
    unittest.TextTestRunner(verbosity=2).run(suite)