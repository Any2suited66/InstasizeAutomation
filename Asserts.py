from appium.webdriver.common.touch_action import TouchAction

class PhotoLibraryAsserts(object):

    def __init__(self, driver):
        self.driver = driver

    def assertTrue(self, is_displayed, param):
        pass

    def allPhotosButton(self):
        allPhotosButton = self.driver.find_element_by_id("btnShowAlbumsList")
        self.assertTrue(allPhotosButton.is_displayed, "Failed, Check for crash")

    def tvFilterLevel(self):
        tvFilterLevel = self.driver.find_element_by_id("tvFilterLevel")
        self.assertTrue(tvFilterLevel.is_displayed, "Failed, Check for crash")


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


class GridPageAsserts(object):

    def __init__(self, driver):
        self.driver = driver

    def assertTrue(self, is_displayed, param):
        pass

    def settingsIconAssert(self):
        settingsIcon = self.driver.find_element_by_id("ibSettingsIcon")
        self.assertTrue(settingsIcon.is_displayed, "Failed, check for crash manually")
