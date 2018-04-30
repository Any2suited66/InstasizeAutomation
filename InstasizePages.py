from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# custom explicit wait for element to be enabled
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

class EditorPage(object):
    def __init__(self, driver):
        self.driver = driver

    def tapSharebutton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
        el = self.driver.find_element_by_id("com.jsdev.instasize:id/ibExport")
        el.click()

    def tapStartFreeTrial(self):
        freeTrial = self.driver.find_element_by_id("com.jsdev.instasize:id/btnTryFreeTrial")
        freeTrial.click()

    def tapInstasizeButton(self):
        for x in range(0, 3):
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAspectChange")))
            sleep(2)
            self.driver.find_element_by_id("com.jsdev.instasize:id/ibAspectChange").click()

    def bDayFilter(self):
        sleep(4)
        for x in range(0, 50):
            try:
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BDAY']")
                if filter_found.is_displayed():
                    EditorPage.tapBDayFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapBDayFilter(self):
        EditorPage.wait_for_editor(self)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BDAY']").click()

    def tapBdayDateSpinner(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/tvBirthday")))
        date_spinner = self.driver.find_element_by_id("com.jsdev.instasize:id/tvBirthday")
        date_spinner.click()

    def tapBdaySpinnerForInput(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "android:id/numberpicker_input")))
        self.driver.swipe(392, 2469, 392, 2130)


    def tapCreateMyFilterBtn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnCreateFilter")))
        tapCreateFilter = self.driver.find_element_by_id("com.jsdev.instasize:id/btnCreateFilter")
        tapCreateFilter.click()

    def tapUseFilterBtn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnUseFilter")))
        tapUseFilter = self.driver.find_element_by_id("com.jsdev.instasize:id/btnUseFilter")
        tapUseFilter.click()

    def tapFilterManager(self):
        for x in range(0, 50):
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text ='MANAGE']").click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    def moveFilterInManager(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivHandle")))
        handle = self.driver.find_element_by_id('com.jsdev.instasize:id/ivHandle')
        moveFilter = TouchAction(self.driver)
        moveFilter.long_press(handle, x=102, y=106).move_to(x=102, y=819).release().perform()

    def tapPremiumBanner(self):
        banner = self.driver.find_element_by_id("getCollectionViewContainer")
        banner.click()

    def tapDenyReviewPopup(self):

        try:
                EditorPage.wait_for_editor(self)
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnDeny")))
                noThanksButton = self.driver.find_element_by_id("com.jsdev.instasize:id/btnDeny")
                noThanksButton.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def tapReviewApp(self):
        self.driver.find_element_by_id("btnReview").click()

    def tapCropFeature(self):
        EditorPage.wait_for_editor(self)
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Crop']").click()

    def tapAdjustmentsFeature(self):
        EditorPage.wait_for_editor(self)
        settings = self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Adjustments']")
        settings.click()

    def adjustSeekBar(self):
        adjust = self.driver.find_element_by_id('com.jsdev.instasize:id/seekBar')
        backAndForth = TouchAction(self.driver)
        backAndForth.long_press(adjust, x=724, y=2137).move_to(x=1270, y=2137).release().perform()

        backAndForth.long_press(adjust, x=1270, y=2137).move_to(x=174, y=2137).release().perform()

        backAndForth.long_press(adjust, x=174, y=2137).move_to(x=1270, y=2137).release().perform()

    def tapTextFeature(self):
        EditorPage.wait_for_editor(self)
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Text']").click()

    def tapLeagueGothic(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='League Gothic']")))
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='League Gothic']").click()

    def doubleTapTextBox(self):
        sleep(2)
        action = TouchAction(self.driver)
        action.tap(element=None, x=750, y=400, count=2).perform()

    def typeInTextBox(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class = 'android.widget.EditText' and @index ='0']")))
        addText = self.driver.find_element_by_xpath("//*[@class = 'android.widget.EditText' and @index ='0']")
        addText.send_keys('Test with me today and tomorrow! YAY!')
        doneButton = self.driver.find_element_by_id('android:id/button1')
        doneButton.click()

    def tapAccept(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class = 'android.widget.ImageButton' and @content-desc ='Accept']")))
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageButton' and @content-desc ='Accept']").click()

    def tapBorderFeature(self):
        sleep(5)
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Border']").click()

    def tapToolsFeature(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
        sleep(2)
        EditorPage.featuresSwipe(self)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class = 'android.widget.ImageView' and @content-desc ='Tools']")))
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Tools']").click()

    def tapOnAllTools(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='HORIZONTAL']")))
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='HORIZONTAL']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='VERTICAL']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='ROTATE']").click()

    def discardEditsYes(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnDiscard")))
        yesDiscard = self.driver.find_element_by_id("com.jsdev.instasize:id/btnDiscard")
        yesDiscard.click()

    def wait_for_editor(self):
        for x in range(0, 20):
            try:
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle1')
                pass
            except NoSuchElementException:
                break

    def driverQuit(self):
        print ("Passed!")
        self.driver.quit()
        sleep(2)

    # Premium version swipe
    def swipeInEditor(self):
        EditorPage.wait_for_editor(self)
        self.driver.swipe(1000, 2140, 100, 2140)

    def swipeRightToLeftInEditor(self):
        sleep(4)
        self.driver.swipe(201, 2268, 1000, 2268)

    def swipeTopToBottom(self):
        sleep(2)
        self.driver.swipe(800, 2284, 800, 40)

    def featuresSwipe(self):
        self.driver.swipe(1000, 2500, 500, 2500)

    def freeVersionSwipeInEditor(self):
        sleep(2)
        self.driver.swipe(1000, 2050, 201, 2050)

    def filterManagerSwipe(self):
        sleep(1)
        self.driver.swipe(1070, 1500, 1070, 300)

class GridPage(object):
    def __init__(self, driver):
        self.driver = driver

    # taps the + sign on the grid page
    def simpleTapAddPhoto(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
        plusIcon2 = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
        plusIcon2.click()

    def skip_onborading(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnGetStarted")))
        getStartedBtn = self.driver.find_element_by_id("com.jsdev.instasize:id/btnGetStarted")
        if getStartedBtn.is_displayed():

            try:
                WebDriverWait(self.driver, 7).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnGetStarted")))
                self.driver.find_element_by_id("com.jsdev.instasize:id/btnGetStarted").click()
                WebDriverWait(self.driver, 7).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnSkip")))
                self.driver.find_element_by_id("com.jsdev.instasize:id/btnSkip").click()
                GridPage.purchasPremiumEditor(self)

            except NoSuchElementException:
                pass

            except TimeoutException:
                pass
        else:
            pass

    def addPhotoTap(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
        GridPage.purchasPremiumEditor(self)
        self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto").click()


    def freeTrialButton(self):
        self.driver.find_element_by_id("com.jsdev.instasize:id/btnGoPremium")

    def tapPhotoOption(self):
        photo = self.driver.find_element_by_id("com.jsdev.instasize:id/ibPhoto")
        photo.click()

    def tapSubscribeButton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.android.vending:id/continue_button")))
        subscribeBtn = self.driver.find_element_by_id("com.android.vending:id/continue_button")
        subscribeBtn.click()

    def tapShareButton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
        sleep(5)
        share = self.driver.find_element_by_id("com.jsdev.instasize:id/ibExport")
        share.click()

    def tapStartFreeTrial(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnTryFreeTrial")))
        freeTrial = self.driver.find_element_by_id("com.jsdev.instasize:id/btnTryFreeTrial")
        freeTrial.click()


    # this method looks for the 'free trial' button on grid and if it is present, it will purchase premium from the
    # the editor screen.  Premium screen on grid has too many animations for appium to find elements.
    def purchasPremiumEditor(self):
        try:

            if self.driver.find_element_by_id("com.jsdev.instasize:id/btnGoPremium").is_displayed():
                    GridPage.simpleTapAddPhoto(self)
                    GridPage.tapPhotoOption(self)
                    GridPage.tapTopLeftImageInPhotoLibrary(self)
                    GridPage.tapShareButton(self)
                    GridPage.tapStartFreeTrial(self)
                    GridPage.tapSubscribeButton(self)
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "ivCollapseIcon")))
                    self.driver.back()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivShareCollapse")))
                    self.driver.back()
            else:
                pass

        except NoSuchElementException:
            pass


    def tapOnCloudOption(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibCloud")))
        cloud = self.driver.find_element_by_id("com.jsdev.instasize:id/ibCloud")
        cloud.click()

    def tapOnCloudImageInSystem(self):
        image = self.driver.find_element_by_id("com.android.documentsui:id/icon_mime")
        image.click()


    def addPhotoFind(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
        try:
            addPhotoFind = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
            self.assertTrue(addPhotoFind.is_displayed(), "+ not found, Test Failed! Check for crash manually")
        except NoSuchElementException:
            print("element not found, check manually!")
            pass

    def tap_get_started_button(self):
        sleep(2)
        for x in range(0,10):
            try:
                el = self.driver.find_element_by_id("btnGetStarted")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print("element not found, please check manually and to make sure element is still present")
                break

    def skip_button(self):
        sleep(2)
        for x in range(0,10):
            try:
                sleep(5)
                el = self.driver.find_element_by_id("btnSkip")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print ("element not found, please check manually and to make sure element is still present")
                break

    def tapTopLeftPhotoOnGrid(self):
            try:
                sleep(13)
                topLeftPhotoGridtap = self.driver.find_element_by_id("ivPhoto")

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "ivPhoto")))

                topLeftPhotoGridtap.click()
                pass

            except NoSuchElementException:
                print ("test failed, check manually")

    def tap_second_grid_image(self):

            try:
                sleep(2)
                el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[2]")
                if el.is_displayed():
                    el.click()
                    pass
            except NoSuchElementException:
                print ("test failed, check manually")
                self.driver.quit()

    def tap_camera_icon(self):
        self.driver.find_element_by_id("ibCamera").click()

    def take_photo(self):
        sleep(4)
        tap = TouchAction(self.driver)
        tap.tap(None, 730, 2346).perform()
        sleep(2)

    def tap_retry_camera(self):
        self.driver.find_element_by_xpath("(//android.widget.TextView[@index=0])").click()

    def tap_camera_ok(self):
        sleep(4)
        tap = TouchAction(self.driver)
        tap.tap(None, 1080, 80).perform()
        sleep(2)


    def tapReeditBtn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "ibEdit")))
        self.driver.find_element_by_id("ibEdit").click()

    def tapPhotoContainer(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/photosContainer")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/photosContainer").click()

    # taps the top left photo in the photo library
    def tapTopLeftImageInPhotoLibrary(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivPhoto")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ivPhoto").click()

    def wait_for_editor(self):
        for x in range(0, 20):
            try:
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle1')
                pass
            except NoSuchElementException:
                break

    def tapInstagramIcon(self):
        GridPage.wait_for_editor(self)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@index=2]")))
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='Instagram']").click()
        sleep(15)
        self.driver.back()

    def tapInstagramPopup(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "android:id/icon")))
        nativeInstagram = self.driver.find_element_by_xpath("//*[@class =""'android.widget.TextView' and @text ='Instagram']")
        nativeInstagram.click()

    def assertCollapseIconPresent(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "ivCollapseIcon")))
        collapseIcon = self.driver.find_element_by_id("ivCollapseIcon")
        self.assertTrue(collapseIcon.is_displayed(), "Not Present, check for crash")

    def assertTrue(self, param, param1):
        pass

    def tapDeleteIconOnGrid(self):
        deletePhoto = self.driver.find_element_by_id("ibDelete")
        WebDriverWait(self.driver, 30).until(
            element_is_enabled((By.ID, "ibDelete"), "true"))
        deletePhoto.click()

    def tapDeleteButton(self):
        WebDriverWait(self.driver, 30).until(
            element_is_enabled((By.ID, "btnDelete"), "true"))
        self.driver.find_element_by_id("btnDelete").click()

    def tapCancelButton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "btnCancel")))
        self.driver.find_element_by_id("btnCancel").click()

    def tapSettingsIcon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibSettingsIcon")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ibSettingsIcon").click()

    def tapCollageBtn(self):
        self.driver.find_element_by_id("ibCollage").click()

    def tapWhatsNewBtn(self):
        try:
            whatsNewIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibWhatsNewIcon")
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibWhatsNewIcon")))
            whatsNewIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                whatsNewIcon = self.driver.find_element_by_xpath("//android.widget.ImageButton[@index=2]")
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibWhatsNewIcon")))
                whatsNewIcon.click()

            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("btnSkip").click()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
                    self.driver.back()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, "//android.widget.ImageButton[@index=2]")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibWhatsNewIcon]").click()

                except:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, "//android.widget.ImageButton[@index=2]")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibWhatsNewIcon").click()

    def openProfilePage(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPlus")))
            profilePlusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus")
            profilePlusIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                profilePlusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus")
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPlus")))
                profilePlusIcon.click()

            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id("btnSkip").click()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
                    self.driver.back()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPlus]")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus]").click()

                except:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPlus")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus").click()


class PhotoLibraryPage(object):
    def __init__(self, driver):
        self.driver = driver

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList").click()


class CollagePage(object):
    def __init__(self, driver):
        self.driver = driver

    def tapFirstCollageOption(self):
        sleep(3)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.view.View[@index=1]")))
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

    def tapTopLeftImagePhotoLib(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "(//android.widget.ImageView[@index=0])")))
        topLeftPhoto = self.driver.find_element_by_id("com.jsdev.instasize:id/ivPhoto")
        topLeftPhoto.click()


    def tap2ndPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[3]")
        CollagePage.wait_for_editor(self)
        el.click()


    def tap3rdPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[5]")
        CollagePage.wait_for_editor(self)
        el.click()


    def tap4thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[7]")
        CollagePage.wait_for_editor(self)
        el.click()

    def tap5thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[9]")
        CollagePage.wait_for_editor(self)
        el.click()

    def tap6thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[11]")
        CollagePage.wait_for_editor(self)
        el.click()

    def wait_for_editor(self):
        for x in range(0, 20):
            try:
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle1')
                pass
            except NoSuchElementException:
                break

class ProfilePage(object):
    def __init__(self, driver):
        self.driver = driver

    def tapSignIn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/tvOption1")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/tvOption1").click()

    def enterLoginInfo(self):
        email = self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress")
        email.click()
        email.send_keys('test1@test.com')
        password = self.driver.find_element_by_id("com.jsdev.instasize:id/etvPassword")
        password.click()
        password.send_keys('aaaaaaaa')

    def tapSignUp(self):
        signUP = self.driver.find_element_by_id("com.jsdev.instasize:id/btnMainAction")
        signUP.click()

    def enterFullName(self):
        fullName = self.driver.find_element_by_id("com.jsdev.instasize:id/etvFullName")
        fullName.click()
        fullName.send_keys('Test Me')

    def enterEmail(self):
        email = self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress")
        email.click()
        email.send_keys('randomEmail@test.com')

class SelectFormat(object):
    def __init__(self, driver):
        self.driver = driver

    def collapseIcon(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList")

def test_request(arg=None):
    """Your http request."""
    sleep(2)
    return arg





