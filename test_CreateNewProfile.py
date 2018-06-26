import unittest
from ExportHelper import FilterExportHelper

from InstasizePages import ProfilePage, GridPage
from Asserts import GridPageAsserts

from DriverBuilder7zero import DriverBuilderAndroid


class test_CreateNewProfile(unittest.TestCase):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_create_new_profile(self):
        filter_export_helper = FilterExportHelper()
        profilePage = ProfilePage(self.driver)
        grid_page = GridPage(self.driver)

        filter_export_helper.setupFilter()
        filter_export_helper.filterExportInstagram()
        profilePage.openProfilePage()
        profilePage.name_generator()
        profilePage.email_generator()
        profilePage.pw_generator()
        profilePage.tapSignUp()
        grid_page.GDPR_skip()
        profilePage.tapSignUp()

        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.premium_badge_assert()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_CreateNewProfile)
    unittest.TextTestRunner(verbosity=2).run(suite)
