import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from ExportHelper import FilterExportHelper
import inspect

def _by_link_text():
    pass


class FilterExportTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def findCallerMethod(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        print(filename)

    def test_filter_uploads(self):

        filterExportHelper = FilterExportHelper()

        filterExportHelper.filter_exports()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)