class EditorPage(object):

    def __init__(self, driver):
        self.driver = driver

    def sharebutton(self):
        self.driver.find_element_by_id("ibExport").click()

    def h1filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

        #
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