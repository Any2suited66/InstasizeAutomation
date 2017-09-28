import unittest

import self as self
from appium import webdriver
from time import sleep
from page_objects import PageObject, PageElement


class Grid(object):
    def __init__(self, driver):
        self.driver = driver

    def addPhoto(self):
        self.driver.find_element_by_id("ibAddPhoto").click()

    def photoContainers(self):
        self.driver.find_element_by_id("photosContainer").click()

    def topLeftPhoto(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index=0]").click()

    def instagramIcon(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@index=1]").click()

    def instagramPopup(self):
        try: self.driver.find_element_by_id("android:id/icon").click()
        except: self.driver.back()

