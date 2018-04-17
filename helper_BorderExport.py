from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts


def _by_link_text():
    pass


class BordersFeatureTest(object):

    def __init__(self, driver):
        self.driver = driver



    def test_borders(self):

        borderList = ["//android.widget.TextView[@text='XOXO']",       "//android.widget.TextView[@text='COLOR']",
                       "//android.widget.TextView[@text='SPRING']",     "//android.widget.TextView[@text='MARBLE']",    "//android.widget.TextView[@text='MERICA']",
                       "//android.widget.TextView[@text='HOLIDAY']",    "//android.widget.TextView[@text='AUTUMN']",    "//android.widget.TextView[@text='WOOD']",
                       "//android.widget.TextView[@text='FLORAL']",     "//android.widget.TextView[@text='COSMIC']",    "//android.widget.TextView[@text='CAMO']",
                       "//android.widget.TextView[@text='BW I']",       "//android.widget.TextView[@text='POLKA DOT']", "//android.widget.TextView[@text='BW II']",
                       "//android.widget.TextView[@text='ANIMAL']",     "//android.widget.TextView[@text='NEBULA']",    "//android.widget.TextView[@text='CHEVRON']",
                       "//android.widget.TextView[@text='TIMBER']",     "//android.widget.TextView[@text='GC']",        "//android.widget.TextView[@text='BW III']",
                       "//android.widget.TextView[@text='GOLD']",       "//android.widget.TextView[@text='GLITTER']",   "//android.widget.TextView[@text='GEOMETRIC']",
                       "//android.widget.TextView[@text='LINE']",       "//android.widget.TextView[@text='TRIBAL']",    "//android.widget.TextView[@text='PINK']"]

        tryExcepts = TryExcepts
        gridPage = GridPage
        editorPage = EditorPage

        for x in borderList:
            gridPage.addPhotoTap(self.driver)
            gridPage.tapPhotoContainer(self.driver)
            gridPage.tapTopLeftImageInPhotoLibrary(self.driver)
            editorPage.tapDenyReviewPopup()
            editorPage.tapBorderFeature()
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/ibExport"))))
                    border = self.driver.find_element_by_xpath("(""%s"")" % x)
                    border.click()
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, ("//android.widget.RelativeLayout[@index='4']"))))
                    applyBorder = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='4']")
                    applyBorder.click()
                    editorPage.tapAccept()
                    editorPage.tapSharebutton()
                    break
                except NoSuchElementException:
                    editorPage = EditorPage(self.driver)
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass

            gridPage.tapInstagramIcon(self.driver)
            tryExcepts.instagramSystemPopup(self.driver)
            sleep(5)
            self.driver.back()