import os
import os
import unittest
from appium import webdriver
from time import sleep
from GridPage import Grid
from selenium.common.exceptions import NoSuchElementException



class Filters(object):

    def __init__(self, driver):
        self.driver = driver

    def sharebutton(self):
        self.driver.find_element_by_id("ibExport").click()

    def h1filter(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='H1']").click()

    def reviewPopup(self):
        self.driver.find_element_by_id("btnDeny").click()

    def filterLevel(self):
        self.driver.find_element_by_id("tvFilterLevel")

        #
        # h2Filter = PageElement(xpath="//android.widget.TextView[@text='H2']")
        # h3Filter = PageElement(xpath="//android.widget.TextView[@text='H3']")
        # v1Filter = PageElement(xpath="//android.widget.TextView[@text='V1']")
        # v2Filter = PageElement(xpath="//android.widget.TextView[@text='V2']")
        # v3Filter = PageElement(xpath="//android.widget.TextView[@text='V3']")
