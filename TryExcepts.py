from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
            pass

    def instagramSystemPopup(self):
        while True:
            if self.driver.find_element_by_id('com.jsdev.instasize:id/ivShareCollapse').is_displayed():
                sleep(1)
                return True

            else:
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "android:id/icon")))
                    self.driver.find_element_by_xpath(
                        "//*[@class = 'android.widget.TextView' and @text ='Feed']").click()
                    break

                except NoSuchElementException:
                    break

                except TimeoutException:
                    break









