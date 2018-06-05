import unittest
from pixelXLtests.pixelXLDriverBuilder import DriverBuilderAndroid

from InstasizePages import GridPage, EditorPage
from ExportHelper import FilterExportHelper
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class test_SigleImageFilterExport(unittest.TestCase):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_filter_exports(self):

        normalFilterList = ["//android.widget.TextView[@text='C3']",
                            "//android.widget.TextView[@text='C2']",
                            "//android.widget.TextView[@text='C1']",
                            "//android.widget.TextView[@text='H1']",
                            "//android.widget.TextView[@text='RADIO']",
                            "//android.widget.TextView[@text='H2']",
                            "//android.widget.TextView[@text='H3']", "//android.widget.TextView[@text='F1']",
                            "//android.widget.TextView[@text='F2']",
                            "//android.widget.TextView[@text='F3']", "//android.widget.TextView[@text='A1']",
                            "//android.widget.TextView[@text='A2']",
                            "//android.widget.TextView[@text='A3']", "//android.widget.TextView[@text='R1']",
                            "//android.widget.TextView[@text='R2']",
                            "//android.widget.TextView[@text='R3']", "//android.widget.TextView[@text='V1']",
                            "//android.widget.TextView[@text='V2']",
                            "//android.widget.TextView[@text='V3']", "//android.widget.TextView[@text='KOTO']",
                            "//android.widget.TextView[@text='PIKE']",
                            "//android.widget.TextView[@text='AZUL']", "//android.widget.TextView[@text='CALICO']",
                            "//android.widget.TextView[@text='FRONT']",
                            "//android.widget.TextView[@text='TACOMA']", "//android.widget.TextView[@text='ECHO']",
                            "//android.widget.TextView[@text='CRUZ']",
                            "//android.widget.TextView[@text='FLUME']", "//android.widget.TextView[@text='TIMBER']",
                            "//android.widget.TextView[@text='ARYA']",
                            "//android.widget.TextView[@text='TARIUS']", "//android.widget.TextView[@text='ROSE']",
                            "//android.widget.TextView[@text='BACH']",
                            "//android.widget.TextView[@text='LOFT']", "//android.widget.TextView[@text='BLOOM']",
                            "//android.widget.TextView[@text='JUKE']",
                            "//android.widget.TextView[@text='WALES']", "//android.widget.TextView[@text='ROKI']",
                            "//android.widget.TextView[@text='HILLS']",
                            "//android.widget.TextView[@text='LATCH']", "//android.widget.TextView[@text='FIN']",
                            "//android.widget.TextView[@text='LOON']",
                            "//android.widget.TextView[@text='LANA']", "//android.widget.TextView[@text='OSAKA']",
                            "//android.widget.TextView[@text='ROOT']",
                            "//android.widget.TextView[@text='KAUAI']", "//android.widget.TextView[@text='SPARK']",
                            "//android.widget.TextView[@text='RISE']",
                            "//android.widget.TextView[@text='MERIT']", "//android.widget.TextView[@text='COAST']",
                            "//android.widget.TextView[@text='TIKI']",
                            "//android.widget.TextView[@text='OAK']", "//android.widget.TextView[@text='TOKYO']",
                            "//android.widget.TextView[@text='BARK']",
                            "//android.widget.TextView[@text='LINCOLN']", "//android.widget.TextView[@text='1989']",
                            "//android.widget.TextView[@text='HIRO']",
                            "//android.widget.TextView[@text='HULA']", "//android.widget.TextView[@text='WAVES']",
                            "//android.widget.TextView[@text='KAYAK']",
                            "//android.widget.TextView[@text='RIO']", "//android.widget.TextView[@text='NEWPORT']",
                            "//android.widget.TextView[@text='NOVA']",
                            "//android.widget.TextView[@text='WASATCH']", "//android.widget.TextView[@text='MARKET']",
                            "//android.widget.TextView[@text='MADRID']",
                            "//android.widget.TextView[@text='FLUX']", "//android.widget.TextView[@text='CELSIUS']",
                            "//android.widget.TextView[@text='PETRA']",
                            "//android.widget.TextView[@text='ORGANIC']", "//android.widget.TextView[@text='NOMAD']",
                            "//android.widget.TextView[@text='ALTA']",
                            "//android.widget.TextView[@text='BALTIC']", "//android.widget.TextView[@text='JUNO']",
                            "//android.widget.TextView[@text='ATHENS']"]

        gridPage = GridPage(self.driver)

        gridPage.skip_onboarding()

        filterExportHelper = FilterExportHelper()

        filterExportHelper.addAllFiltersFromManager()

        for x in normalFilterList:

            filterExportHelper.setupFilter()
            # taps on the filter
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/ibExport"))))
                    filter = self.driver.find_element_by_xpath("(""%s"")" % x)
                    filter.click()
                    break
                except NoSuchElementException:
                    editorPage = EditorPage(self.driver)
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass

            filterExportHelper.filterExportInstagram()

            sleep(5)
            self.driver.back()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_SigleImageFilterExport)
    unittest.TextTestRunner(verbosity=2).run(suite)