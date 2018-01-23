from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditorPage(object):
    def __init__(self, driver):
        self.driver = driver

    def sharebutton(self):
        for _ in xrange(10):
            try:
                self.driver.swipe(600, 500, 602, 500)
                el = self.driver.find_element_by_id('ibExport')
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "test failed, test manually"
                self.driver.quit()

    def instasizButton(self):
        self.driver.find_element_by_id("ibAspectChange").click()

    def findCoastFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='COAST']")
                if filter_found.is_displayed():
                    EditorPage.tapCoastFilter(self)
                    break

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapKayakFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='KAYAK']").click()

    def lincolnFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LINCOLN']")
                if filter_found.is_displayed():
                    EditorPage.tapLincolnFilter(self)
                    break

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
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

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapNineteen89Filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='1989']").click()

    def celsiusFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']")
                if filter_found.is_displayed():
                    EditorPage.tapCelsiusFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapCelsiusFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='CELSIUS']").click()

    def petraFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']")
                if filter_found.is_displayed():
                    EditorPage.tapPetraFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapPetraFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='PETRA']").click()

    def organicFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']")
                if filter_found.is_displayed():
                    EditorPage.tapOrganicFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapOrganicFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ORGANIC']").click()

    def nomadFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']")
                if filter_found.is_displayed():
                    EditorPage.tapNomadFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapNomadFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='NOMAD']").click()

    def altaFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']")
                if filter_found.is_displayed():
                    EditorPage.tapAltaFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapAltaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ALTA']").click()

    def balticFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']")
                if filter_found.is_displayed():
                    EditorPage.tapBalticFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapBalticFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BALTIC']").click()

    def junoFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']")
                if filter_found.is_displayed():
                    EditorPage.tapJunoFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapJunoFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='JUNO']").click()

    def latchFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='LATCH']")
                if filter_found.is_displayed():
                    EditorPage.tapLatchFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapLatchFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LATCH']").click()

    def hulaFilter(self):
        for _ in xrange(50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']")
                if filter_found.is_displayed():
                    EditorPage.tapHulaFilter(self)
                    break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapHulaFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HULA']").click()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def giveAReviewButtonTap(self):
        self.driver.find_element_by_id("btnReview").click()

    def driverQuit(self):
        print "Filter Passed!"
        sleep(3)
        self.driver.quit()
        sleep(5)

    def swipeInEditor(self):
                sleep(2)
                self.driver.swipe(1000, 2268, 201, 2268)
                self.driver.implicitly_wait(2)


class GridPage(object):
    def __init__(self, driver):
        self.driver = driver

    # taps the + sign on the grid page
    def addPhotoTap(self):
        # had to add this try/except to take care of the premium popup screen.
        # if premium popup screen is removed please delete this try/except to reduce testing time
        for _ in xrange(5):
            try:
                el = self.driver.find_element_by_id("btnGetStarted")
                if el.is_displayed():
                    el.click()
                    sleep(2)
                    pass
            except NoSuchElementException:
                    print "element not found, please check manually and to make sure element is still present"
                    sleep(2)
                    pass

        for _ in xrange(5):
            try:
                sleep(3)
                el = self.driver.find_element_by_id("btnSkip")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                self.driver.find_element_by_id("btnGetStarted").click()
                pass

        self.driver.find_element_by_id("ibAddPhoto").click()

    def addPhotoFind(self):
        sleep(3)
        try:
            addPhotoFind = self.driver.find_element_by_id("ibAddPhoto")
            self.assertTrue(addPhotoFind.is_displayed(), "+ not found, Test Failed! Check for crash manually")
        except NoSuchElementException:
            print("element not found, check manually!")
            pass

    def tap_get_started_button(self):
        sleep(2)
        for _ in xrange(10):
            try:
                el = self.driver.find_element_by_id("btnGetStarted")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "element not found, please check manually and to make sure element is still present"
                break

    def skip_button(self):
        sleep(2)
        for _ in xrange(10):
            try:
                sleep(5)
                el = self.driver.find_element_by_id("btnSkip")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "element not found, please check manually and to make sure element is still present"
                break

    def topLeftPhotoGridtap(self):
        for _ in xrange(10):
            try:
                sleep(5)
                topLeftPhotoGridtap = self.driver.find_element_by_id("ivPhoto")
                if topLeftPhotoGridtap.is_displayed():
                    topLeftPhotoGridtap.click()
                    break
            except NoSuchElementException:
                print "test failed, check manually"



    def second_grid_image(self):
        for _ in xrange(10):
            try:
                sleep(20)
                el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[2]")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "test failed, check manually"
                self.driver.quit()




    def tap_camera_icon(self):
        self.driver.find_element_by_id("ibCamera").click()

    def take_photo(self):
        self.driver.find_element_by_id("MENUID_SHUTTER").click()

    def tap_retry_camera(self):
        self.driver.find_element_by_xpath("(//android.widget.TextView[@index=0])").click()

    def tap_camera_ok(self):
        self.driver.find_element_by_xpath("(//android.widget.TextView[@index=1])").click()

    def reeditButtontap(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("ibEdit").click()

    def collapseIconFind(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def photoContainers(self):
        self.driver.find_element_by_id("photosContainer").click()

    # top left photo in the photo library
    def topLeftPhoto(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index=0]").click()
        sleep(5)

    def instagramIcon(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@index=2]").click()

    def instagramPopup(self):
        self.driver.find_element_by_id("android:id/icon").click()

    def collapseIconAssert(self):
        collapseIcon = self.driver.find_element_by_id("ivCollapseIcon")
        self.assertTrue(collapseIcon.is_displayed(), "Not Present, check for crash")

    def assertTrue(self, param, param1):
        pass

    def deleteIconTap(self):
        self.driver.find_element_by_id("ibDelete").click()

    def deleteButtonTap(self):
        self.driver.find_element_by_id("btnDelete").click()

    def cancelButtonTap(self):
        self.driver.find_element_by_id("btnCancel").click()

    def settingsIconTap(self):
        self.driver.find_element_by_id("ibSettingsIcon").click()

    def collageButtonTap(self):
        self.driver.find_element_by_id("ibCollage").click()


class PhotoLibraryPage(object):
    def __init__(self, driver):
        self.driver = driver

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList").click()


class CollagePage(object):
    def __init__(self, driver):
        self.driver = driver

    def tapFirstCollageOption(self):
        if self.driver.find_element_by_xpath("//android.view.View[@index=1]").is_displayed():
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@index=1]")))
            self.driver.find_element_by_xpath("//android.view.View[@index=1]").click()

    def tap2ndCollageOption(self):
        sleep(2)
        self.driver.find_element_by_xpath("(//android.view.View[@index=0])[2]").click()
        sleep(3)

    def tap3rdCollageOption(self):
        sleep(2)
        self.driver.swipe(1360, 200, 160, 200)
        self.driver.find_element_by_xpath("(//android.view.View[@index=0])[3]").click()

    def tap4thCollageOption(self):
        sleep(2)
        self.driver.swipe(1360, 200, 160, 200)
        self.driver.swipe(1360, 200, 460, 200)
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View[@index=1]").click()

    def tap5thCollageOption(self):
        sleep(2)
        self.driver.swipe(1360, 200, 160, 200)
        sleep(2)
        self.driver.swipe(1360, 200, 260, 200)
        sleep(2)
        self.driver.swipe(1360, 200, 760, 200)
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View[@index=2]").click()

    def tap6thCollageOption(self):
        sleep(2)
        self.driver.swipe(1360, 200, 160, 200)
        sleep(2)
        self.driver.swipe(1360, 200, 260, 200)
        sleep(2)
        self.driver.swipe(1360, 200, 260, 200)
        sleep(2)
        self.driver.swipe(1360, 200, 160, 200)
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View[@index=0]").click()



    def topLeftPhoto(self):
        sleep(2)
        self.driver.find_element_by_id("ivPhoto").click()

    def tap2ndPhoto(self):
        sleep(2)
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[2]").click()

    def tap3rdPhoto(self):
        sleep(3)
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[3]").click()

    def tap4thPhoto(self):
        sleep(3)
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[4]").click()

    def tap5thPhoto(self):
        sleep(3)
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[5]").click()

    def tap6thPhoto(self):
        sleep(3)
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[6]").click()




class SelectFormat(object):
    def __init__(self, driver):
        self.driver = driver

    def collapseIcon(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList")
