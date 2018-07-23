from time import sleep
import signal
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
from Common_lists import filter_list

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
        EditorPage.wait_for_editor(self)
        el = self.driver.find_element_by_id("com.jsdev.instasize:id/ibExport")
        el.click()

    def tapStartFreeTrial(self):
        freeTrial = self.driver.find_element_by_id("com.jsdev.instasize:id/btnTryFreeTrial")
        freeTrial.click()

    def tapInstasizeButton(self):
        EditorPage.wait_for_editor(self)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAspectChange")))
        instasizeButton = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAspectChange")
        for x in range(0, 5):
            sleep(1)
            instasizeButton.click()

    def bDayFilter(self):
        sleep(4)
        while True:
            try:
                sleep(2)
                filter_found = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BDAY']")
                if filter_found.is_displayed():
                    EditorPage.tapBDayFilter(self)
                    break

            except:
                EditorPage.swipeInEditor(self)

    def tapBDayFilter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BDAY']").click()

    def tapBdayDateSpinner(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/tvBirthday")))
        date_spinner = self.driver.find_element_by_id("com.jsdev.instasize:id/tvBirthday")
        date_spinner.click()

    def swipe_bday_spinner(self):
        page = self.driver.page_source
        print(page)
        sleep(2)
        self.driver.swipe(360, 2400, 360, 1900)

    def tapBdaySpinnerForInput(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "android:id/numberpicker_input")))
        spinner = self.driver.find_element_by_id("android:id/numberpicker_input")
        self.driver.set_value(spinner, 'Dec')
        self.driver.find_element_by_id("android:id/numberpicker_input").click()

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
        # waits for IS button to be present on screen
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAspectChange")))
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
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
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

    def dismiss_popup(self):
        try:
            WebDriverWait(self.driver, 7).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
            if self.driver.find_element_by_id('com.jsdev.instasize:id/ivCollapseIcon').is_displayed:
                dismiss = self.driver.find_element_by_id('com.jsdev.instasize:id/ivCollapseIcon')
                dismiss.click()

            else:
                raise Exception

        except:
            pass

    def purchase_premium_editor_popup(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibCollapse")))
            click_try = self.driver.find_element_by_id('com.jsdev.instasize:id/btnAction')
            click_try.click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.android.vending:id/continue_button")))
            subscribe_btn = self.driver.find_element_by_id('com.android.vending:id/continue_button')
            subscribe_btn.click()
            EditorPage.dismiss_popup(self)

        except TimeoutException:
            EditorPage.dismiss_popup(self)

        except NoSuchElementException:
            EditorPage.dismiss_popup(self)

    def purchase_premium_banner(self):
        try:
            if self.driver.find_element_by_id('com.jsdev.instasize:id/rlEditorGoPremiumBannerContainer').is_displayed:
                self.driver.find_element_by_id('com.jsdev.instasize:id/rlEditorGoPremiumBannerContainer').click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnTryFree")))
                self.driver.find_element_by_id('com.jsdev.instasize:id/btnTryFree').click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.android.vending:id/continue_button")))
                self.driver.find_element_by_id('com.android.vending:id/continue_button').click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCollapseIcon').click()
            else:
                raise TimeoutException
        except:
            pass

    def wait_for_editor(self):
        while True:
            try:
                sleep(1)
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle4')
                pass
            except NoSuchElementException:
                break

    def wait_for_border_dwnld(self):
        while True:
            try:
                if self.driver.find_element_by_id('android:id/alertTitle').is_displayed():
                    return True

            except NoSuchElementException:
                break

    def driverQuit(self):
        print ("Passed!")
        self.driver.quit()
        sleep(2)

    # Premium version swipe
    def swipeInEditor(self):
        editor_page = EditorPage(self.driver)
        editor_page.wait_for_editor()
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
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
            plusIcon2 = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
            plusIcon2.click()

        except TimeoutException:
            print('what happened? better check the test flow manually!')


    def enter_age_screen(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/cbAge")))
            age_check_box = self.driver.find_element_by_id('com.jsdev.instasize:id/cbAge')
            if age_check_box.is_displayed:

                age_check_box.click()

                data_check_box = self.driver.find_element_by_id('com.jsdev.instasize:id/cbData')
                data_check_box.click()

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnAccept")))
                accept_btn = self.driver.find_element_by_id('com.jsdev.instasize:id/btnAccept')
                accept_btn.click()
            else:
                pass
        except TimeoutException:
            pass
        except NoSuchElementException:
            pass

    def skip_onboarding(self):

        GridPage.enter_age_screen(self)
        try:
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
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def addPhotoTap(self):
        try:
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
            self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto").click()
            sleep(2)
            GridPage.GDPR_skip(self)
        except TimeoutException:
            pass


    def GDPR_skip(self):
        gridPage = GridPage(self.driver)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/cbCombined")))
            tap_checkbox = self.driver.find_element_by_id("com.jsdev.instasize:id/cbCombined")
            tap_checkbox.click()
            gridPage.tap_agree_to_continue()
        except:
            pass

    def tap_agree_to_continue(self):
        sleep(2)
        self.driver.find_element_by_id("com.jsdev.instasize:id/btnAccept").click()

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
        EditorPage.wait_for_editor(self.driver)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
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
                    GridPage.GDPR_skip(self)
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

    def purchase_premium_grid_screen(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnTryFreeTrial")))
            if self.driver.find_element_by_id('com.jsdev.instasize:id/btnTryFreeTrial').is_displayed:
                self.driver.find_element_by_id('com.jsdev.instasize:id/btnTryFreeTrial').click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.android.vending:id/continue_button")))
                self.driver.find_element_by_id('com.android.vending:id/continue_button').click()
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCollapseIcon').click()
            else:
                raise Exception
        except:
            pass

    def tapOnCloudOption(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibCloud")))
        cloud = self.driver.find_element_by_id("com.jsdev.instasize:id/ibCloud")
        cloud.click()

    def tapOnCloudImageInSystem(self):

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "com.android.documentsui:id/toolbar")))

            image = self.driver.find_element_by_id("com.android.documentsui:id/date")
            image.click()

        except TimeoutException:
            print('check test flow in case android version was updated')

        except NoSuchElementException:
            print('check test flow in case android version was updated')

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
                sleep(1)
                self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle1')
                pass
            except NoSuchElementException:
                break

    def tapInstagramIcon(self):
        GridPage.wait_for_editor(self)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@index=2]")))
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='Instagram']").click()

        while True:
            try:
                sleep(2)
                if self.driver.find_element_by_id('com.jsdev.instasize:id/ivCircle4').is_displayed():
                    sleep(1)
                    pass
                else:
                    raise Exception

            except:
                try:
                    sleep(2)
                    self.driver.find_element_by_xpath(
                        "//*[@class = 'android.widget.TextView' and @text ='Feed']").click()
                    break
                except NoSuchElementException:
                    break
                    pass


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
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibDelete")))
        deletePhoto = self.driver.find_element_by_id("com.jsdev.instasize:id/ibDelete")
        deletePhoto.click()

    def tapDeleteButton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnDelete")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/btnDelete").click()

    def tapCancelButton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "btnCancel")))
        self.driver.find_element_by_id("btnCancel").click()

    def tapSettingsIcon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibSettingsIcon")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ibSettingsIcon").click()

    def tapCollageBtn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibCollage")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ibCollage").click()

    def tapWhatsNewBtn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibSettingsIcon")))
        try:
            whatsNewIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibWhatsNewIcon")
            whatsNewIcon.click()

        except NoSuchElementException:
            print('whats new button not found, check manually')

    def tap_back(self):
        self.driver.back()

class SettingsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def HDExportButtonTap(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/switchExportImageQuality")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/switchExportImageQuality").click()

    def tap_instagram_icon(self):
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivInstagram")))
        instagram_icon = self.driver.find_element_by_id('com.jsdev.instasize:id/ivInstagram')
        instagram_icon.click()

    def tap_facebook_icon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivInstagram")))
        facebook_icon = self.driver.find_element_by_id("com.jsdev.instasize:id/ivFacebook")
        facebook_icon.click()

    def tap_twitter_icon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivTwitter")))
        twitter_icon = self.driver.find_element_by_id("com.jsdev.instasize:id/ivTwitter")
        twitter_icon.click()

    def tap_youtube_icon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivYoutube")))
        youtube_icon = self.driver.find_element_by_id("com.jsdev.instasize:id/ivYoutube")
        youtube_icon.click()

    def tap_snapchat_icon(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivSnapchat")))
        snapchat_icon = self.driver.find_element_by_id("com.jsdev.instasize:id/ivSnapchat")
        snapchat_icon.click()

    def settings_premium_purchase(self):
        editor_page = EditorPage(self.driver)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@class =""'android.widget.TextView' and @text ='Settings']")))
            start_trial = self.driver.find_element_by_id("com.jsdev.instasize:id/btnTryFreeTrial")
            start_trial.click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.android.vending:id/continue_button")))
            subscribe_btn = self.driver.find_element_by_id('com.android.vending:id/continue_button')
            subscribe_btn.click()
            editor_page.dismiss_popup()

        except NoSuchElementException:
            pass
        except TimeoutException:
            pass



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

    def tap_profile_image(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPhoto")))
            profile_image = self.driver.find_element_by_id('com.jsdev.instasize:id/ibPhoto')
            profile_image.click()

        except:
            pass

    def tap_first_image_in_gallery(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivPhoto")))
            first_image = self.driver.find_element_by_id('com.jsdev.instasize:id/ivPhoto')
            first_image.click()
        except:
            pass

    def tap_done_in_gallery(self):
        done_btn = self.driver.find_element_by_id('com.jsdev.instasize:id/btnDone')
        done_btn.click()

    def tapSignIn(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/tvOption1")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/tvOption1").click()

    def enterLoginInfo(self):
        email = self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress")
        email.click()
        email.send_keys('tyler@munkee.co')
        password = self.driver.find_element_by_id("com.jsdev.instasize:id/etvPassword")
        password.click()
        password.send_keys('aaaaaaaa')

    def tapSignUp(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnMainAction")))
            signUP = self.driver.find_element_by_id("com.jsdev.instasize:id/btnMainAction")
            sleep(2)
            signUP.click()
        except:
            pass

    def enterFullName(self):
        fullName = self.driver.find_element_by_id("com.jsdev.instasize:id/etvFullName")
        fullName.click()
        fullName.send_keys('Test Me')

    def enterEmail(self):
        email = self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress")
        email.click()
        email.send_keys('randomEmail@test.com')

    def openProfilePage(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibPlus")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus").click()

    def tap_full_name(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/etvFullName")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/etvFullName").click()

    def tap_email(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/etvEmailAddress")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress").click()

    def tap_pw(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/etvPassword")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/etvPassword").click()

    def name_generator(self, N=6):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/etvFullName")))
        randomName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        fullNameBox = self.driver.find_element_by_id("com.jsdev.instasize:id/etvFullName")
        fullNameBox.send_keys(randomName)

    def pw_generator(self, N=8):
        randomPW = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        pWBox = self.driver.find_element_by_id("com.jsdev.instasize:id/etvPassword")
        pWBox.send_keys(randomPW)

    def email_generator(self, N=8):
        randomEmail = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        emailBox = self.driver.find_element_by_id("com.jsdev.instasize:id/etvEmailAddress")
        emailBox.send_keys(''.join('test@' + randomEmail + '.com'))

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


class Helper_Methods(object):

    def __init__(self, driver):
        self.driver = driver

    def collageFilterSetup(self):
        gridPage = GridPage(self.driver)
        collagePage = CollagePage(self.driver)
        editorPage = EditorPage(self.driver)
        gridPage.addPhotoTap()
        gridPage.tapCollageBtn()
        collagePage.tapTopLeftImagePhotoLib()
        collagePage.tap2ndPhoto()
        collagePage.tap3rdPhoto()
        collagePage.tap4thPhoto()
        collagePage.tap5thPhoto()
        collagePage.tap6thPhoto()
        collagePage.tap2ndCollageOption()
        editorPage.tapDenyReviewPopup()

    def addAllFiltersFromManager(self):
        from Common_lists import filter_manager_list
        helper_methods = Helper_Methods(self.driver)
        editorPage = EditorPage(self.driver)


        helper_methods.setupFilter()

        try:
            for x in range(0, 13):
                editorPage.swipeInEditor()
            athens_filter = self.driver.find_element_by_xpath("//adnroid.widget.TextView[@text='ATHENS']")
            if athens_filter.is_displayed:
                self.driver.back()
                sleep(2)
                editorPage.tapAccept()

        except NoSuchElementException:
            editorPage.tapFilterManager()
            pass

        # searches for filter
        for a in filter_manager_list:
            for x in range(0, 30):
                try:
                    filter = self.driver.find_element_by_xpath("(""%s"")" % a)
                    print("(""%s"")" % a)
                    filter.click()
                    break
                except NoSuchElementException:
                    editorPage.filterManagerSwipe()
                    pass

        editorPage.tapAccept()
        editorPage.wait_for_editor()
        self.driver.back()
        editorPage.discardEditsYes()

    def filterExportInstagram(self):
        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)

        editorPage.purchase_premium_banner()
        editorPage.tapSharebutton()
        editorPage.dismiss_popup()
        gridPage.purchase_premium_grid_screen()
        gridPage.tapInstagramIcon()
        sleep(5)
        self.driver.back()

    def setupFilter(self):
        editorPage = EditorPage(self.driver)
        gridPage = GridPage(self.driver)

        # taps on the + icon
        gridPage.addPhotoTap()
        # taps on the native photos container
        gridPage.tapPhotoContainer()
        # taps on the top left photo
        gridPage.tapTopLeftImageInPhotoLibrary()
        # taps 'No thanks' on app review popup
        editorPage.tapDenyReviewPopup()



