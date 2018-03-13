from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def SettingsButton(self):
        # had to add this try/except to take care of the premium popup screen.
        # if premium popup screen is removed please delete this try/except to reduce testing time

        try:
            sleep(5)
            self.driver.find_element_by_id("com.jsdev.instasize:id/btnGetStarted").click()
            sleep(3)
            self.driver.find_element_by_id("com.jsdev.instasize:id/btnSkip").click()
            sleep(2)
            self.driver.find_element_by_id("com.jsdev.instasize:id/ibSettingsIcon").click()

        except NoSuchElementException:
            sleep(3)
            self.driver.find_element_by_id("com.jsdev.instasize:id/ibSettingsIcon").click()



    def HDExportButtonTap(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/switchExportImageQuality")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/switchExportImageQuality").click()
