import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from SingleImageExportHelper import SingleImageExportHelper

def _by_link_text():
    pass


class FilterExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_filter_uploads(self):

        singleImageExportHelper = SingleImageExportHelper(self.driver)

        singleImageExportHelper.filter_exports()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)