from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pixelXLtests.pixelXLDriverBuilder import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
import unittest
from time import sleep
from ExportHelper import FilterExportHelper

def _by_link_text():
    pass


class BordersFeatureTest(unittest.TestCase):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_borders(self):

        borderList = ["//android.widget.TextView[@text='XOXO']",       "//android.widget.TextView[@text='COLOR']",      "//android.widget.TextView[@text='VIBES']",
                       "//android.widget.TextView[@text='SPRING']",     "//android.widget.TextView[@text='MARBLE']",    "//android.widget.TextView[@text='MERICA']",
                       "//android.widget.TextView[@text='HOLIDAY']",    "//android.widget.TextView[@text='AUTUMN']",    "//android.widget.TextView[@text='WOOD']",
                       "//android.widget.TextView[@text='FLORAL']",     "//android.widget.TextView[@text='COSMIC']",    "//android.widget.TextView[@text='CAMO']",
                       "//android.widget.TextView[@text='BW I']",       "//android.widget.TextView[@text='POLKA DOT']", "//android.widget.TextView[@text='BW II']",
                       "//android.widget.TextView[@text='ANIMAL']",     "//android.widget.TextView[@text='NEBULA']",    "//android.widget.TextView[@text='CHEVRON']",
                       "//android.widget.TextView[@text='TIMBER']",     "//android.widget.TextView[@text='GC']",        "//android.widget.TextView[@text='BW III']",
                       "//android.widget.TextView[@text='GOLD']",       "//android.widget.TextView[@text='GLITTER']",   "//android.widget.TextView[@text='GEOMETRIC']",
                       "//android.widget.TextView[@text='LINE']",       "//android.widget.TextView[@text='TRIBAL']",    "//android.widget.TextView[@text='PINK']"]

        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onboarding()

        for x in borderList:
            filterExportHelper.setupFilter()
            editorPage.tapBorderFeature()
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    editorPage.wait_for_editor()
                    border = self.driver.find_element_by_xpath("(""%s"")" % x)
                    border.click()
                    WebDriverWait(self.driver, 120).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/seekBar"))))
                    borderElement = self.driver.find_element_by_xpath("//android.widget.ImageView[@index='4']")
                    borderElement.click()
                    editorPage.adjustSeekBar()
                    editorPage.tapAccept()
                    filterExportHelper.filterExportInstagram()
                    break
                except NoSuchElementException:
                    editorPage = EditorPage(self.driver)
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass
                except TimeoutException:
                    self.driver.back()

            sleep(5)
            self.driver.back()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BordersFeatureTest)
    unittest.TextTestRunner(verbosity=2).run(suite)