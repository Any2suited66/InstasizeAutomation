from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep


class SettingsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def SettingsButton(self):
        # had to add this try/except to take care of the premium popup screen.
        # if premium popup screen is removed please delete this try/except to reduce testing time
        for _ in xrange(5):
            try:
                el = self.driver.find_element_by_id("btnGetStarted")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "element not found, please check manually and to make sure element is still present"
                break

        for _ in xrange(5):
            try:
                sleep(3)
                el = self.driver.find_element_by_id("btnSkip")
                if el.is_displayed():
                    el.click()
                    break
            except NoSuchElementException:
                print "element not found, please check manually and to make sure element is still present"
                break
            finally:
                self.driver.find_element_by_id('ibSettingsIcon').click()

    def HDExportButtonTap(self):
        self.driver.find_element_by_id('switchExportImageQuality').click()
