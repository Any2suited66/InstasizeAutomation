from selenium.common.exceptions import NoSuchElementException


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
            self.driver.find_element_by_id("icon").click()
        except NoSuchElementException:
            print("Not required on this version of android")