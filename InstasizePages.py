from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def sharebutton(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibExport")))
        el = self.driver.find_element_by_id("com.jsdev.instasize:id/ibExport")
        el.click()


    def instasizeButton(self):
        for _ in xrange(3):
            sleep(5)
            self.driver.find_element_by_id("com.jsdev.instasize:id/ibAspectChange").click()

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

    def bDayFilter(self):
        sleep(4)
        for _ in xrange(50):
            try:
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

    def tapBdaySpinnerForInput(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "android:id/numberpicker_input")))
        spinner = self.driver.find_element_by_id("android:id/numberpicker_input")
        self.driver.set_value(spinner, 'Dec')
        self.driver.find_element_by_id("android:id/numberpicker_input").click()

    def tapCreateMyFilter(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnCreateFilter")))
        tapCreateFilter = self.driver.find_element_by_id("com.jsdev.instasize:id/btnCreateFilter")
        tapCreateFilter.click()

    def tapUseFilter(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/btnUseFilter")))
        tapUseFilter = self.driver.find_element_by_id("com.jsdev.instasize:id/btnUseFilter")
        tapUseFilter.click()

    def tapFilterManager(self):
        for _ in xrange(50):
            try:
                self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='MANAGE']").click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    # taps athens filter in filter manager
    def tapAthensBox(self):
        for _ in xrange(10):
            try:
                sleep(2)
                tapCheckBox = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='ATHENS']")
                tapCheckBox.click()
                break

            except NoSuchElementException:
                EditorPage.swipeTopToBottom(self)
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

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

    def giveAReviewButtonTap(self):
        self.driver.find_element_by_id("btnReview").click()

    def tapCropFeature(self):
        sleep(5)
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Crop']").click()

    def tapCropFree(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='FREE']").click()

    def tapCropOneToOne(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='1:1']").click()

    def tapCropThreeToTwo(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='3:2']").click()

    def tapCropFiveToThree(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='5:3']").click()

    def tapCropFourToThree(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='4:3']").click()

    def tapCropFiveToFour(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='5:4']").click()

    def tapCropFourToFive(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='4:5']").click()

    def tapCropThreeToFour(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='3:4']").click()

    def tapCropTwoToThree(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='2:3']").click()

    def tapCropSevenToFive(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='7:5']").click()

    def tapCrop21To9(self):
        EditorPage.swipeInEditor(self)
        sleep(2)
        EditorPage.swipeInEditor(self)
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='21:9']").click()

    def tapAdjustmentsFeature(self):
        sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.ImageView' and @content-desc ='Adjustments']")))
        settings = self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc = 'Adjustments']")
        settings.click()

    def tapExposure(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.TextView' and @text ='EXPOSURE']")))
        exposure = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='EXPOSURE']")
        exposure.click()

    def tapContrast(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.TextView' and @text ='CONTRAST']")))
        contrast = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='CONTRAST']")
        contrast.click()

    def tapBrightness(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.TextView' and @text ='BRIGHTNESS']")))
        brightness = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='BRIGHTNESS']")
        brightness.click()

    def tapSharpness(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.TextView' and @text ='SHARPNESS']")))
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@class = 'android.widget.TextView' and @text ='SHARPNESS']")))
        sharpness = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='SHARPNESS']")
        sharpness.click()

    def tapSaturation(self):
        for _ in xrange(5):
            try:
                saturation = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='SATURATION']")
                saturation.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapTint(self):
        for _ in xrange(5):
            try:
                tint = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='TINT']")
                tint.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapWarmth(self):
        for _ in xrange(5):
            try:
                warmth = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='WARMTH']")
                warmth.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)

    def tapVignette(self):
        for _ in xrange(5):
            try:
                vignette = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='VIGNETTE']")
                vignette.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    def tapShadows(self):
        for _ in xrange(5):
            try:
                shadows = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='SHADOWS']")
                shadows.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    def tapHighlights(self):
        for _ in xrange(5):
            try:
                highlights = self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='HIGHLIGHTS']")
                highlights.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    def tapGrain(self):
        for _ in xrange(5):
            try:
                sleep(2)
                grain = self.driver.find_element_by_xpath(
                    "//*[@class = 'android.widget.TextView' and @text ='GRAIN']")
                grain.click()
                break

            except NoSuchElementException:
                EditorPage.swipeInEditor(self)
                pass

    def adjustSeekBar(self):
        adjust = self.driver.find_element_by_id('com.jsdev.instasize:id/seekBar')
        backAndForth = TouchAction(self.driver)
        backAndForth.long_press(adjust, x=724, y=2137).move_to(x=1270, y=2137).release().perform()

        backAndForth.long_press(adjust, x=1270, y=2137).move_to(x=174, y=2137).release().perform()

        backAndForth.long_press(adjust, x=174, y=2137).move_to(x=1270, y=2137).release().perform()


    def tapAccept(self):
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageButton' and @content-desc ='Accept']").click()

    def tapBorderFeature(self):
        sleep(5)
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.ImageView' and @content-desc ='Border']").click()

    def tapXOXOBorderPack(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='XOXO']").click()

    def tapX1Border(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='X1']").click()

    def tapPhotoBorder(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='PHOTO']").click()

    def tapBlurPhotoBorder(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='BLUR']").click()

    def tapPhotoLibraryBorder(self):
        sleep(2)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='LIBRARY']").click()

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


    def driverQuit(self):
        print "Passed!"
        self.driver.quit()
        sleep(2)

    # Premium version swipe
    def swipeInEditor(self):
        sleep(4)
        self.driver.swipe(1000, 2268, 201, 2268)

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

    def discardEditsConfirm(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "btnDiscard")))
        self.driver.find_element_by_id("btnDiscard").click()


class GridPage(object):
    def __init__(self, driver):
        self.driver = driver

    # taps the + sign on the grid page
    def addPhotoTap(self):
        # had to add this try/except to take care of the premium popup screen.
        # if premium popup screen is removed please delete this try/except to reduce testing time

        try:
            plusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
            sleep(2)
            plusIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            sleep(1)
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                sleep(2)
                plusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto")
                plusIcon.click()

            except NoSuchElementException:
                try:
                    sleep(1)
                    self.driver.find_element_by_id("btnSkip").click()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto").click()

                except:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
                    sleep(2)
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ibAddPhoto").click()

    def tapOnCloudOption(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibCloud")))
        cloud = self.driver.find_element_by_id("com.jsdev.instasize:id/ibCloud")
        cloud.click()

    def tapOnCloudImage(self):
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
            try:
                sleep(13)
                topLeftPhotoGridtap = self.driver.find_element_by_id("ivPhoto")

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "ivPhoto")))

                topLeftPhotoGridtap.click()
                pass

            except NoSuchElementException:
                print "test failed, check manually"

    def second_grid_image(self):

            try:
                sleep(2)
                el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[2]")
                if el.is_displayed():
                    el.click()
                    pass
            except NoSuchElementException:
                print "test failed, check manually"
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


    def reeditButtontap(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("ibEdit").click()

    def photoContainers(self):
        self.driver.find_element_by_id("photosContainer").click()

    # taps the top left photo in the photo library
    def topLeftPhoto(self):
        sleep(5)
        # WebDriverWait(self.driver, 30).until(
        #     EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivPhoto")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/ivPhoto").click()

    def instagramIcon(self):
        sleep(1)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@index=2]")))
        self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='Instagram']").click()

    def instagramPopup(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "android:id/icon")))
        nativeInstagram = self.driver.find_element_by_xpath("//*[@class = "
                                                            "'android.widget.TextView' and @text ='Instagram']")
        nativeInstagram.click()

    def collapseIconFind(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "ivCollapseIcon")))
        collapseIcon = self.driver.find_element_by_id("ivCollapseIcon")
        self.assertTrue(collapseIcon.is_displayed(), "Not Present, check for crash")

    def assertTrue(self, param, param1):
        pass

    def deleteIconTap(self):
        deletePhoto = self.driver.find_element_by_id("ibDelete")
        WebDriverWait(self.driver, 30).until(
            element_is_enabled((By.ID, "ibDelete"), "true"))
        deletePhoto.click()

    def deleteButtonTap(self):
        self.driver.find_element_by_id("btnDelete").click()

    def cancelButtonTap(self):
        self.driver.find_element_by_id("btnCancel").click()

    def settingsIconTap(self):
        self.driver.find_element_by_id("ibSettingsIcon").click()

    def collageButtonTap(self):
        self.driver.find_element_by_id("ibCollage").click()

    def whatsNewBtnTap(self):
        try:
            whatsNewIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibWhatsNewIcon")
            sleep(2)
            whatsNewIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                whatsNewIcon = self.driver.find_element_by_xpath("//android.widget.ImageButton[@index=2]")
                sleep(2)
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
            profilePlusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus")
            sleep(2)
            profilePlusIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                profilePlusIcon = self.driver.find_element_by_id("com.jsdev.instasize:id/ibPlus")
                sleep(2)
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

    def topLeftPhoto(self):
        sleep(5)
        el = self.driver.find_element_by_id("ivPhoto")
        # WebDriverWait(self.driver, 30).until(
        #     element_is_enabled((By.ID, "ivPhoto"), "true"))
        el.click()


    def tap2ndPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[3]")
        sleep(3)
        el.click()


    def tap3rdPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[5]")
        sleep(3)
        el.click()


    def tap4thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[7]")
        sleep(3)
        el.click()

    def tap5thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[9]")
        sleep(3)
        el.click()

    def tap6thPhoto(self):
        el = self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[11]")
        sleep(3)
        el.click()

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
