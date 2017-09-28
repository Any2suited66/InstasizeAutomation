import unittest

import self as self
from appium import webdriver
from time import sleep
from page_objects import PageObject, PageElement


class Grid(object):
    def __init__(self, driver):
        self.driver = driver

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList").click()