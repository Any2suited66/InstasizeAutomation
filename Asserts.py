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


