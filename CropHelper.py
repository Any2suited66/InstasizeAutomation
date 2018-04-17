from time import sleep

from selenium.common.exceptions import NoSuchElementException

from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts


class CropHelper(object):
    def __init__(self, driver):
        self.driver = driver

    def cropFeatures(self):


        cropFeatureList = ["//android.widget.TextView[@text ='FREE']", "//android.widget.TextView[@text ='1:1']",
                           "//android.widget.TextView[@text ='3:2']", "//android.widget.TextView[@text ='5:3']",
                           "//android.widget.TextView[@text ='4:3']", "//android.widget.TextView[@text ='5:4']",
                           "//android.widget.TextView[@text ='4:5']", "//android.widget.TextView[@text ='3:4']",
                           "//android.widget.TextView[@text ='2:3']", "//android.widget.TextView[@text ='7:5']",
                           "//android.widget.TextView[@text ='21:9']"]

        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)

        for a in cropFeatureList:
            gridPage.addPhotoTap()
            gridPage.tapPhotoContainer()
            gridPage.tapTopLeftImageInPhotoLibrary()
            editorPage.tapDenyReviewPopup()
            editorPage.tapCropFeature()
            for x in range(0, 10):
                try:
                    cropFeature = self.driver.find_element_by_xpath("(""%s"")" % a)
                    cropFeature.click()
                    editorPage.tapAccept()
                    editorPage.tapSharebutton()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editorPage.swipeInEditor()

            # Taps on Instagram icon
            gridPage = GridPage(self.driver)
            gridPage.tapInstagramIcon()

            # Searches for Instagram android popup on bottom of screen
            tryExceots = TryExcepts(self.driver)
            tryExceots.instagramSystemPopup()

            sleep(5)
            self.driver.back()


