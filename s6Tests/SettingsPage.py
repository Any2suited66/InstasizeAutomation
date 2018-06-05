from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def HDExportButtonTap(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "com.jsdev.instasize:id/switchExportImageQuality")))
        self.driver.find_element_by_id("com.jsdev.instasize:id/switchExportImageQuality").click()
