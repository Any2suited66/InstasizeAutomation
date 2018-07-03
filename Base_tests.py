from InstasizePages import GridPage, EditorPage, ProfilePage, Helper_Methods, SettingsPage
from Common_lists import border_list, filter_list
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Asserts import GridPageAsserts, SettingsPageAsserts


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
        editor_page = EditorPage(self.driver)

        helper_methods.addAllFiltersFromManager()

        for x in filter_list:
            helper_methods.collageFilterSetup()
            # taps on the filter
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    filter = self.driver.find_element_by_xpath("(""%s"")" % x)
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, ("(""%s"")" % x))))
                    filter.click()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editor_page.swipeInEditor()
                    pass
            helper_methods.filterExportInstagram()

        grid_page_asserts.settingsIconAssert()

    def create_new_profile_test(self):
        profilePage = ProfilePage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        grid_page = GridPage(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.name_generator()
        profilePage.email_generator()
        profilePage.pw_generator()
        profilePage.tapSignUp()
        grid_page.GDPR_skip()

        gridPageAsserts.premium_badge_assert()

    def crop_feature_test(self):
        from Common_lists import cropFeatureList
        helper_methods = Helper_Methods(self.driver)
        editor_page = EditorPage(self.driver)
        for a in cropFeatureList:
            helper_methods.setupFilter()
            editor_page.tapCropFeature()
            for x in range(0, 10):
                try:
                    cropFeature = self.driver.find_element_by_xpath("(""%s"")" % a)
                    cropFeature.click()
                    editor_page.tapAccept()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editor_page.swipeInEditor()

            helper_methods.filterExportInstagram()

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
        from Common_lists import adjustmentsList

        helper_methods = Helper_Methods(self.driver)
        editorPage = EditorPage(self.driver)

        helper_methods.setupFilter()
        editorPage.tapAdjustmentsFeature()

        for a in adjustmentsList:
            for x in range(0, 11):
                try:
                    adjustment = self.driver.find_element_by_xpath("(""%s"")" % a)
                    sleep(2)
                    adjustment.click()
                    editorPage.adjustSeekBar()
                    editorPage.tapAccept()
                    break

                except NoSuchElementException:
                    editorPage.swipeInEditor()

        helper_methods.filterExportInstagram()

    def bday_filter_test(self):
        grid_page_asserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.bDay_filter_iteration()
        grid_page_asserts.settingsIconAssert()

    def delete_image(self):
        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        # Taps on the top left image on the grid
        gridPage.tapTopLeftPhotoOnGrid()
        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()
        # Taps on cancel
        gridPage.tapCancelButton()
        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()
        # Taps on delete button in popup
        gridPage.tapDeleteButton()
        # Asserts the image was deleted successfully
        gridPageAsserts.gridPagePhotoNotPresent()

    def import_from_cloud(self):
        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)
        editor_page = EditorPage(self.driver)

        # taps on the + icon
        gridPage.addPhotoTap()
        # taps on cloud option
        gridPage.tapOnCloudOption()
        # taps on the second image
        gridPage.tapOnCloudImageInSystem()
        editor_page.purchase_premium_editor_popup()
        helper_methods.filterExportInstagram()
        gridPageAsserts.settingsIconAssert()

    def instasize_btn_test(self):
        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.setupFilter()
        # taps on the yellow instasize button
        editorPage.tapInstasizeButton()
        helper_methods.filterExportInstagram()
        # Asserts the + button is displayed
        gridPage.addPhotoFind()

    def login_to_profile(self):
        profilePage = ProfilePage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        grid_page = GridPage(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.tapSignIn()
        profilePage.enterLoginInfo()
        profilePage.tapSignUp()
        grid_page.GDPR_skip()

        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.settingsIconAssert()

    def delete_multiple_images(self):
        gridPage = GridPage(self.driver)
        gridPageAsserts = GridPageAsserts(self.driver)
        helper_methods = Helper_Methods(self.driver)

        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        helper_methods.setupFilter()
        helper_methods.filterExportInstagram()
        # Taps on the top left image on the grid
        gridPage.tapTopLeftPhotoOnGrid()
        # taps on the second image on grid screen
        gridPage.tap_second_grid_image()
        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()
        # Taps on cancel
        gridPage.tapCancelButton()
        # Taps on delete icon
        gridPage.tapDeleteIconOnGrid()
        # Taps on delete button in popup
        gridPage.tapDeleteButton()
        gridPageAsserts.settingsIconAssert()

    def non_hd_filter_export(self):
        helper_methods = Helper_Methods(self.driver)
        gridPage = GridPage(self.driver)
        settingsPage = SettingsPage(self.driver)
        editorPage = EditorPage(self.driver)

        helper_methods.addAllFiltersFromManager()
        # taps on the settings icon
        gridPage.tapSettingsIcon()
        # taps the hd switch
        settingsPage.HDExportButtonTap()
        self.driver.back()

        for x in filter_list:

            helper_methods.setupFilter()
            # taps on the filter
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/ibExport"))))
                    filter = self.driver.find_element_by_xpath("(""%s"")" % x)
                    filter.click()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass

            helper_methods.filterExportInstagram()

    def single_image_export_test(self):
        helper_methods = Helper_Methods(self.driver)
        editorPage = EditorPage(self.driver)

        helper_methods.addAllFiltersFromManager()

        for x in filter_list:

            helper_methods.setupFilter()
            # taps on the filter
            print("("'%s'")" % x)
            for i in range(0, 50):
                try:
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.ID, ("com.jsdev.instasize:id/ibExport"))))
                    filter = self.driver.find_element_by_xpath("(""%s"")" % x)
                    filter.click()
                    break
                except NoSuchElementException:
                    sleep(2)
                    editorPage.swipeInEditor()
                    pass

            helper_methods.filterExportInstagram()

    def tools_test(self):
        gridPage = GridPage(self.driver)
        helper_methods = Helper_Methods(self.driver)
        editorPage = EditorPage(self.driver)

        helper_methods.setupFilter()
        # taps the tools feature
        editorPage.tapToolsFeature()
        # taps on all tool features
        editorPage.tapOnAllTools()
        helper_methods.filterExportInstagram()
        # Asserts the + button is displayed
        gridPage.addPhotoFind()

    def test_social_media_icons(self):
        gridPage = GridPage(self.driver)
        settings_page = SettingsPage(self.driver)
        settings_page_asserts = SettingsPageAsserts(self.driver)

        gridPage.tapSettingsIcon()
        settings_page.settings_premium_purchase()
        settings_page.tap_instagram_icon()
        settings_page_asserts.instagram_layout_assert()
        sleep(5)
        self.driver.back()

        settings_page.tap_facebook_icon()
        sleep(5)
        self.driver.back()

        settings_page.tap_twitter_icon()
        settings_page_asserts.twitter_app_assert()
        sleep(5)
        self.driver.back()

        settings_page.tap_youtube_icon()
        settings_page_asserts.youtube_app_assert()
        sleep(5)
        self.driver.back()

        settings_page.tap_snapchat_icon()
        sleep(5)
        self.driver.back()
        sleep(2)
        self.driver.back()

        settings_page_asserts.hd_switch_assert()


#class NegativeBaseTests(object):

#   def incorrect_username_test(self):
