import unittest
from InstasizePages import GridPage

from InstasizePages import ProfilePage
from Asserts import GridPageAsserts

from s7edgeTests.s7edgeDriverBuilder import DriverBuilderAndroid


class test_CreateNewProfile(unittest.TestCase):

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_create_new_profile(self):

        profilePage = ProfilePage(self.driver)
        gridPage = GridPage(self.driver)

        gridPage.skip_onboarding()
        profilePage.openProfilePage()
        profilePage.name_generator()
        profilePage.email_generator()
        profilePage.pw_generator()
        profilePage.tapSignUp()

    def test_premium_badge_assertion(self):
        gridPageAsserts = GridPageAsserts(self.driver)
        gridPageAsserts.premium_badge_assert()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_CreateNewProfile)
    unittest.TextTestRunner(verbosity=2).run(suite)
