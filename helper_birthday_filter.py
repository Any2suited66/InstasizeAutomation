from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from InstasizePages import EditorPage
from InstasizePages import GridPage
from TryExcepts import TryExcepts
from ExportHelper import FilterExportHelper
from DriverBuilder7zero import DriverBuilderAndroid

class BirthdayFilterExport(object):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def birthday_filter_export(self):

        gridPage = GridPage(self.driver)
        editorPage = EditorPage(self.driver)
        filterExportHelper = FilterExportHelper()

        gridPage.skip_onborading()
        gridPage.addPhotoTap()
        gridPage.tapPhotoContainer()
        gridPage.tapTopLeftImageInPhotoLibrary()
        editorPage.tapDenyReviewPopup()
        editorPage.tapBDayFilter()
        editorPage.tapBdayDateSpinner()
        editorPage.tapBdaySpinnerForInput()
        editorPage.tapCreateMyFilterBtn()
        editorPage.tapUseFilterBtn()
        filterExportHelper.filterExportInstagram()


