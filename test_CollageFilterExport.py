import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from ExportHelper import FilterExportHelper


def _by_link_text():
    pass


class CollageExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_collage_filter_uploads(self):

            filterExportHelper = FilterExportHelper()

            filterExportHelper.collage_filter_exports()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CollageExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
