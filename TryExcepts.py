from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TryExcepts(object):

    def __init__(self, driver):
        self.driver = driver

    def reviewPopup(self):
        try:
              self.driver.find_element_by_id("btnDeny").click()
        except NoSuchElementException:
            print('PlayStore review popup did not occur')

    def instagramSystemPopup(self):
        self.driver.implicitly_wait(100)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "android:id/icon")))
            self.driver.find_element_by_xpath("//*[@class = 'android.widget.TextView' and @text ='Instagram']").click()

        except NoSuchElementException:
            print ("Not required on this version of android")
            pass







