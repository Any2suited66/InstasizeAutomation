from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class element_is_enabled(object):
    def __init__(self, locator, is_enabled):
        self.locator = locator
        self.is_enabled = is_enabled

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.is_enabled in element.get_attribute("enabled"):
            return element
        else:
            return False


class PaidEditorPage(object):
    def __init__(self, driver):
        self.driver = driver

    # premium subscription element
    def h1Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapH1Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapH1Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()

    # free version element
    def freeH1Filter(self):
        sleep(5)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']")
                if filter_found.is_displayed():
                    PaidEditorPage.freeTapH1Filter(self)
                    break

            except:
                PaidEditorPage.freeSwipeInEditor(self)

    def freeTapH1Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()

    def h2Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='H2']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapH2Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapH2Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H2']").click()

    def h3Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='H3']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapH3Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapH3Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H3']").click()

    def v1Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='V1']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapV1Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapV1Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='V1']").click()

    def v2Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='V2']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapV2Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapV2Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='V2']").click()

    def v3Filter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='V3']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapV3Filter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapV3Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='V3']").click()

    def kotoFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='KOTO']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapKotoFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapKotoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='KOTO']").click()

    def pikeFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='PIKE']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapPikeFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapPikeFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='PIKE']").click()

    def azulFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='AZUL']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapAzulFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapAzulFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='AZUL']").click()

    def calicoFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='CALICO']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapCalicoFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapCalicoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='CALICO']").click()

    def frontFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='FRONT']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapFrontFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapFrontFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FRONT']").click()

    def tacomaFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='TACOMA']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapTacomaFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapTacomaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TACOMA']").click()

    def echoFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ECHO']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapEchoFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapEchoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ECHO']").click()

    def cruzFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='CRUZ']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapCruzFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapCruzFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='CRUZ']").click()

    def flumeFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUME']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapFlumeFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapFlumeFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUME']").click()

    def timberFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIMBER']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapTimberFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapTimberFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIMBER']").click()

    def aryaFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ARYA']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapAryaFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapAryaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ARYA']").click()

    def tariusFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='TARIUS']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapTariusFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapTariusFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TARIUS']").click()

    def roseFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROSE']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapRoseFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapRoseFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROSE']").click()

    def bachFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BACH']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapBachFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapBachFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BACH']").click()

    def loftFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LOFT']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapLoftFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapLoftFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LOFT']").click()

    def bloomFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BLOOM']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapBloomFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapBloomFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BLOOM']").click()

    def jukeFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUKE']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapJukeFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapJukeFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUKE']").click()
        
    
    def walesFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='WALES']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapWalesFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapWalesFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WALES']").click()
        
    def rokiFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROKI']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapRokiFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapRokiFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROKI']").click()
        
    def hillsFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='HILLS']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapHillsFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapHillsFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HILLS']").click()
        
    def latchFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LATCH']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapLatchFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapLatchFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LATCH']").click()
        
    def finFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='FIN']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapFinFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapFinFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FIN']").click()
        
    def loonFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LOON']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapLoonFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapLoonFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LOON']").click()
        
    def lanaFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LANA']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapLanaFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapLanaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LANA']").click()
        
    def osakaFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='OSAKA']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapOsakaFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapOsakaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='OSAKA']").click()
        
    def rootFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROOT']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapRootFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapRootFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROOT']").click()
        
    def kauaiFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAUAI']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapKauaiFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapKauaiFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAUAI']").click()
        
    def sparkFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='SPARK']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapSparkFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapSparkFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='SPARK']").click()
        
    def riseFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='RISE']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapRiseFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapRiseFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='RISE']").click()
        
    def meritFilter(self):
        PaidEditorPage.wait_for_editor(self)
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='MERIT']")
                if filter_found.is_displayed():
                    PaidEditorPage.tapMeritFilter(self)
                    break

            except:
                PaidEditorPage.swipeInEditor(self)

    def tapMeritFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='MERIT']").click()


    def swipeInEditor(self):
        WebDriverWait(self.driver, 30).until(
            element_is_enabled((By.ID, "ibExport"), "true"))
        self.driver.swipe(1000, 2268, 201, 2268)
        self.driver.implicitly_wait(2)

    def freeSwipeInEditor(self):
        self.driver.swipe(900, 2050, 220, 2050)
        self.driver.implicitly_wait(2)

    def wait_for_editor(self):
        self.driver.implicitly_wait(5)