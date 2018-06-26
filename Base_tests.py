

from InstasizePages import GridPage, EditorPage, ProfilePage, Helper_Methods
from Common_lists import border_list
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Asserts import GridPageAsserts






class BaseTests(object):


    def __init__(self, driver):
        self.driver = driver


    def test_new_profile(self):
        profilePage = ProfilePage(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.name_generator()
        profilePage.email_generator()
        profilePage.pw_generator()
        profilePage.tapSignUp()
        gridPageAsserts = GridPageAsserts(self)
        gridPageAsserts.premium_badge_assert()

    def test_collage_feature(self):

        helper_methods = Helper_Methods(self)
        grid_page_asserts = GridPageAsserts(self)

        helper_methods.addAllFiltersFromManager()
        helper_methods.iterate_filters_collage()
        grid_page_asserts.settingsIconAssert()

    def camera_test(self):
        gridPage = GridPage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        editor_page = EditorPage(self.driver)
        gridPage.purchasPremiumEditor()
        gridPage.addPhotoTap()
        # taps on the camera icon
        gridPage.tap_camera_icon()
        # takes a picture
        gridPage.take_photo()
        # taps on ok
        gridPage.tap_camera_ok()
        editor_page.purchase_premium_editor_popup()
        helper_methods.filterExportInstagram()
        gridPage.addPhotoFind()

    def collage_test(self):
        grid_page_asserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.iterate_filters_collage()
        grid_page_asserts.settingsIconAssert()

    def create_new_profile_test(self):
        profilePage = ProfilePage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.name_generator()
        profilePage.email_generator()
        profilePage.pw_generator()
        profilePage.tapSignUp()
        gridPageAsserts.premium_badge_assert()

    def crop_feature_test(self):
        helper_methods = Helper_Methods(self.driver)
        grid_page_asserts = GridPageAsserts(self.driver)

        helper_methods.iterate_crop_options()
        grid_page_asserts.settingsIconAssert()

    def border_feature_test(self):
        editorPage = EditorPage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        grid_page_asserts = GridPageAsserts(self.driver)

        for x in border_list:
            helper_methods.setupFilter()
            editorPage.tapBorderFeature()
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    editorPage.wait_for_editor()
                    border = self.driver.find_element_by_xpath("(""%s"")" % x)
                    border.click()
                    WebDriverWait(self.driver, 120).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/seekBar"))))
                    borderElement = self.driver.find_element_by_xpath("//android.widget.ImageView[@index='4']")
                    borderElement.click()
                    editorPage.adjustSeekBar()
                    editorPage.tapAccept()
                    helper_methods.filterExportInstagram()
                    break
                except NoSuchElementException:
                    editorPage = EditorPage(self.driver)
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass
                except TimeoutException:
                    self.driver.back()

        grid_page_asserts.settingsIconAssert()

    def whats_new_test(self):
        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)

        gridPage.tapWhatsNewBtn()
        sleep(5)
        self.driver.back()
        gridPageAsserts.settingsIconAssert()

    def adjustments_feature_test(self):
        gridPageAsserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.iterate_adjustment_options()
        gridPageAsserts.settingsIconAssert()

    def bday_filter_test(self):
        grid_page_asserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.bDay_filter_iteration()
        grid_page_asserts.settingsIconAssert()