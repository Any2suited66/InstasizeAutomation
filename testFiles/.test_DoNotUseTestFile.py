"""Do not use this file for testing.  This is used to experiment with different settings. Ignore this file if it
throws an exception"""



import inspect
import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class FilterExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_filter_uploads(self):

            filterExportHelper = FilterExportHelper()

            filterExportHelper.filter_exports()

            filterExportHelper.filterExportInstagram()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
