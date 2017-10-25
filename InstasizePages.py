from selenium.common.exceptions import NoSuchElementException
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from Asserts import PhotoLibraryAsserts

from os import wait


class EditorPage(object):
    def __init__(self, driver):
        self.driver = driver

    def sharebutton(self):
        self.driver.find_element_by_id("ibExport").click()

    def h1filter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def findCoastFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']")
                if filter_found.is_displayed():
                    EditorPage.tapCoastFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapCoastFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']").click()

    def tikiFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIKI']")
                if filter_found.is_displayed():
                    EditorPage.tapTikiFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapTikiFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIKI']").click()

    def athensFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ATHENS']")
                if filter_found.is_displayed():
                    EditorPage.tapAthensFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapAthensFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ATHENS']").click()

    def oakFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='OAK']")
                if filter_found.is_displayed():
                    EditorPage.tapOakFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapOakFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='OAK']").click()

    def wavesFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='WAVES']")
                if filter_found.is_displayed():
                    EditorPage.tapWavesFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapWavesFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WAVES']").click()

    def tokyoFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='TOKYO']")
                if filter_found.is_displayed():
                    EditorPage.tapTokyoFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapTokyoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TOKYO']").click()

    def kayakFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAYAK']")
                if filter_found.is_displayed():
                    EditorPage.tapKayakFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapKayakFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Kayak']").click()

    def lincolnFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LINCOLN']")
                if filter_found.is_displayed():
                    EditorPage.tapLincolnFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapLincolnFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LINCOLN']").click()

    def rioFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='RIO']")
                if filter_found.is_displayed():
                    EditorPage.tapRioFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapRioFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='RIO']").click()

    def newportFilter(self):
            for _ in xrange(50):
                try:
                    filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='NEWPORT']")
                    if filter_found.is_displayed():
                        EditorPage.tapNewportFilter(self)
                        break

                except:
                    EditorPage.swipeInEditor(self)

    def tapNewportFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NEWPORT']").click()

    def novaFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOVA']")
                if filter_found.is_displayed():
                    EditorPage.tapNovaFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapNovaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOVA']").click()

    def hiroFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='HIRO']")
                if filter_found.is_displayed():
                    EditorPage.tapHiroFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapHiroFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HIRO']").click()

    def wasatchFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='WASATCH']")
                if filter_found.is_displayed():
                    EditorPage.tapWasatchFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapWasatchFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WASATCH']").click()

    def marketFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='MARKET']")
                if filter_found.is_displayed():
                    EditorPage.tapMarketFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapMarketFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='MARKET']").click()

    def radioFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='RADIO']")
                if filter_found.is_displayed():
                    EditorPage.tapRadioFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapRadioFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='RADIO']").click()

    def madridFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='MADRID']")
                if filter_found.is_displayed():
                    EditorPage.tapMadridFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapMadridFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='MADRID']").click()

    def barkFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BARK']")
                if filter_found.is_displayed():
                    EditorPage.tapBarkFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapBarkFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BARK']").click()

    def fluxFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUX']")
                if filter_found.is_displayed():
                    EditorPage.tapFluxFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapFluxFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUX']").click()

    def nineteen89Filter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='1989']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapNineteen89Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='1989']").click()

    def celsiusFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapCelsiusFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']").click()

    def petraFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapPetraFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']").click()

    def organicFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapOrganicFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']").click()

    def nomadFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapNomadFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']").click()

    def altaFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapAltaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']").click()

    def balticFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapBalticFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']").click()

    def junoFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapJunoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']").click()

    def hulaFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']")
                if filter_found.is_displayed():
                    EditorPage.tapNineteen89Filter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapHulaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']").click()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def driverQuit(self):
        sleep(3)
        self.driver.quit()
        sleep(5)

    def swipeInEditor(self):
                self.driver.swipe(1000, 2268, 201, 2268)
                self.driver.implicitly_wait(2)


        # h2Filter = PageElement(xpath="//android.widget.TextView[@text='H2']")
        # h3Filter = PageElement(xpath="//android.widget.TextView[@text='H3']")
        # v1Filter = PageElement(xpath="//android.widget.TextView[@text='V1']")
        # v2Filter = PageElement(xpath="//android.widget.TextView[@text='V2']")
        # v3Filter = PageElement(xpath="//android.widget.TextView[@text='V3']")


class GridPage(object):
    def __init__(self, driver):
        self.driver = driver

    def addPhotoTap(self):
        self.driver.find_element_by_id("ibAddPhoto").click()

    def addPhotoFind(self):
        sleep(3)
        # addPhotoFind = self.driver.find_element_by_id("ibAddPhoto")
        # self.assertTrue(addPhotoFind.is_displayed(), "+ not found, check for crash")
        try:
            addPhotoFind = self.driver.find_element_by_id("ibAddPhoto")
            self.assertTrue(addPhotoFind.is_displayed(), "+ not found, Test Failed! Check for crash manually")
        except:
            self.driver.quit()

    def collapseIconFind(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def photoContainers(self):
        self.driver.find_element_by_id("photosContainer").click()

    def topLeftPhoto(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index=0]").click()
        sleep(5)

    def instagramIcon(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@index=1]").click()

    def instagramPopup(self):
        self.driver.find_element_by_id("android:id/icon").click()

    def collapseIconAssert(self):
        collapseIcon = self.driver.find_element_by_id("ivCollapseIcon")
        self.assertTrue(collapseIcon.is_displayed(), "Not Present, check for crash")

    def assertTrue(self, param, param1):
        pass


class PhotoLibraryPage(object):
    def __init__(self, driver):
        self.driver = driver

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList").click()


class SelectFormat(object):
    def __init__(self, driver):
        self.driver = driver

    def collapseIcon(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList")
