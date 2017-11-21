from appium import webdriver

class SettingsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def SettingsButton(self):
        self.driver.find_element_by_id('ibSettingsIcon').click()

    def HDExportButtonTap(self):
        self.driver.find_element_by_id('switchExportImageQuality').click()
