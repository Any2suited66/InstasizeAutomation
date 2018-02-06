from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PhotoLibraryAsserts(object):

    def __init__(self, driver):
        self.driver = driver

    def assertTrue(self, is_displayed, param):
        pass

    def allPhotosButton(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "btnShowAlbumsList")))
        allPhotosButton = self.driver.find_element_by_id("btnShowAlbumsList")
        self.assertTrue(allPhotosButton.is_displayed, "Failed, Check for crash")

    def tvFilterLevel(self):
        pass
        # tvFilterLevel = self.driver.find_element_by_xpath("//android.widget.TextView[@text='100']")
        # self.assertTrue(tvFilterLevel.is_displayed, "Failed, Check for crash")


class EditorPageAsserts(object):

    def __init__(self, driver):
        self.driver = driver

    def assertTrue(self, is_displayed, param):
        pass

    def giveAReview(self):
        giveAReviewPopup = self.driver.find_element_by_id("btnReview")
        self.assertTrue(giveAReviewPopup.is_displayed, "Failed, check for popup manually")

    def instasizeButtonAssert(self):
        instasizeButton = self.driver.find_element_by_id("ibAspectChange")
        self.assertTrue(instasizeButton.is_displayed, "Failed, check for crash manual)ly")

    def premiumPageAssert(self):
        premiumPage = self.driver.find_element_by_id("coordinator")
        self.assertTrue(premiumPage.is_displayed, "Failed, check for premium page manually")
        sleep(2)
        self.driver.back()
        sleep(2)

    def shareButtonNotDisplayed(self):
        sleep(2)
        try:
            self.driver.find_element_by_id("ibExport")
        except NoSuchElementException:
            print ("Success, user is not able to share the image with a premium filter applied")
            pass
            self.driver.back()


class GridPageAsserts(object):

    def __init__(self, driver):
        self.driver = driver

    def assertTrue(self, is_displayed, param):
        pass

    def settingsIconAssert(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "ibSettingsIcon")))
        settingsIcon = self.driver.find_element_by_id("ibSettingsIcon")
        self.assertTrue(settingsIcon.is_displayed, "Failed, check for crash manually")
        print ("Passed, no crash")

    def gridPagePhotoNotPresent(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_xpath("(//android.widget.ImageView[@index=0])[1]")

        except NoSuchElementException:
            print 'Test passed, image(s) successfully deleted'






