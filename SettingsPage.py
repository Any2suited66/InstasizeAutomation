from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
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
            settingsIcon = self.driver.find_element_by_id("ibSettingsIcon").click()
            sleep(2)
            settingsIcon.click()

        except NoSuchElementException:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "btnGetStarted")))
            sleep(1)
            self.driver.find_element_by_id("btnGetStarted").click()

            try:
                sleep(2)
                settingsIcon = self.driver.find_element_by_id("ibSettingsIcon").click()
                settingsIcon.click()

            except NoSuchElementException:
                try:
                    sleep(1)
                    self.driver.find_element_by_id("btnSkip").click()
                    WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ivCollapseIcon")))
                    self.driver.find_element_by_id("com.jsdev.instasize:id/ivCollapseIcon").click()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "ibSettingsIcon")))
                    self.driver.find_element_by_id("ibSettingsIcon").click()

                except NoSuchElementException:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/ibAddPhoto")))
                    sleep(2)
                    self.driver.find_element_by_id("ibSettingsIcon").click()

    def HDExportButtonTap(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/switchExportImageQuality")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/switchExportImageQuality").click()
