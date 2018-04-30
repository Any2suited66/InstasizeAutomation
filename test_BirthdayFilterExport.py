import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from helper_BorderExport import BordersFeatureTest
import inspect
from helper_birthday_filter import BirthdayFilterExport
def _by_link_text():
    pass


class test_BrithdayFilter(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_crop(self):

        helperBirthdayFilter = BirthdayFilterExport()

        helperBirthdayFilter.birthday_filter_export()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_BrithdayFilter)
    unittest.TextTestRunner(verbosity=2).run(suite)