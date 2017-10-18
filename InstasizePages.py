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

    def coastFilterLocate(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']").is_displayed()

    def findCoastFilter(self):
        for _ in xrange(15):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']")
                if filter_found.is_displayed():
                    EditorPage.tapCoastFilter(self)
                    break

            except NoSuchElementException:
                findFilter = PhotoLibraryAsserts(self)
                findFilter.swipeInEditor(self)

    def tapCoastFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']").click()

    def tikiFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIKI']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def athensFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ATHENS']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def oakFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='OAK']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def wavesFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='WAVES']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def tokyoFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='TOKYO']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def kayakFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAYAK']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def lincolnFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='LINCOLN']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def rioFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='RIO']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def newportFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='NEWPORT']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def novaFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOVA']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def hiroFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='HIRO']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def wasatchFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='WASATCH']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def marketFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='MARKET']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def radioFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='RADIO']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def madridFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='MADRID']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def barkFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='BARK']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def fluxFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUX']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def nineteen89Filter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='1989']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def celsiusFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def petraFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def organicFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def nomadFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def altaFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def balticFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def junoFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def hulaFilter(self):
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']").click()
        except:
            print "Test Failed, check for crash manually and double check if element is located correctly in script"
            self.driver.quit()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def driverQuit(self):
        sleep(3)
        self.driver.quit()
        sleep(5)

    def swipeInEditor(self):
                self.driver.swipe(1202, 2268, 201, 2268)
                self.driver.implicitly_wait(2)

    def tenSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1220, 2268, 250, 2268)
        sleep(2)

    def elevenSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)

    def twelveSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)

    def thirteenSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)

    def fourteenSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)

    def fifteenSwsipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1200, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)
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
