import os
import unittest

import self as self
from appium import webdriver
from time import sleep
from page_objects import PageObject, PageElement

class SelectFormat(object):

    def __init__(self, driver):
        self.driver = driver

    def collapseIcon(self):
        self.driver.find_element_by_id("ivCollapseIcon")

    def allPhotosButton(self):
        self.driver.find_element_by_id("btnShowAlbumsList")