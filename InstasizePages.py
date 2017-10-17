from time import sleep


class EditorPage(object):

    def __init__(self, driver):
        self.driver = driver

    def sharebutton(self):
        self.driver.find_element_by_id("ibExport").click()

    def h1filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()

    def coastFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']").click()

    def tikiFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TIKI']").click()

    def athensFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ATHENS']").click()

    def oakFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='OAK']").click()

    def wavesFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WAVES']").click()

    def tokyoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='TOKYO']").click()

    def kayakFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAYAK']").click()

    def lincolnFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LINCOLN']").click()

    def rioFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='RIO']").click()

    def newportFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NEWPORT']").click()

    def novaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOVA']").click()

    def hiroFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HIRO']").click()

    def wasatchFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WASATCH']").click()

    def marketFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='MARKET']").click()

    def radioFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='RADIO']").click()

    def madridFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='MADRID']").click()

    def barkFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BARK']").click()

    def fluxFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FLUX']").click()

    def nineteen89Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='1989']").click()

    def celsiusFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']").click()

    def petraFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']").click()

    def organicFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']").click()

    def nomadFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']").click()

    def altaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']").click()

    def balticFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']").click()

    def junoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']").click()

    def hulaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']").click()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def oneSwipeRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)

    def twoSwipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)

    def threeSwipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)

    def fourSwipesRtoL(self):
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1202, 2268, 201, 2268)
        sleep(2)
        self.driver.swipe(1190, 2268, 250, 2268)
        sleep(2)

    def fiveSwsipesRtoL(self):
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

    def sixSwsipesRtoL(self):
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

    def sevenSwsipesRtoL(self):
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

    def eightSwsipesRtoL(self):
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
        self.driver.swipe(1210, 2268, 250, 2268)
        sleep(2)

    def nineSwsipesRtoL(self):
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
        self.driver.swipe(1220, 2268, 250, 2268)
        sleep(2)

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
        addPhotoFind = self.driver.find_element_by_id("ibAddPhoto")
        self.assertTrue(addPhotoFind.is_displayed(), "+ not found, check for crash")

    def collapseIconFind(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def photoContainers(self):
        self.driver.find_element_by_id("photosContainer").click()

    def topLeftPhoto(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index=0]").click()

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