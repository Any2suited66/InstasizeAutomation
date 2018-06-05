from time import sleep
import signal
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


# custom explicit wait for element to be enabled
class element_is_enabled(object):
    def __init__(self, locator, is_enabled):
        self.locator = locator
        self.is_enabled = is_enabled

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.is_enabled in element.get_attribute("enabled"):
            return element
        else:
            return False

class EditorPagePixelXL(object):
    def __init__(self, driver):
        self.driver = driver

    def bday_filter_swipe(self):
        sleep(2)
        self.driver.swipe(520, 2077, 520, 1500)