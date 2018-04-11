import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from CropHelper import CropHelper
import inspect

def _by_link_text():
    pass


class Crop_Feature(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_crop(self):

        filterExportHelper = CropHelper(self.driver)

        filterExportHelper.cropFeatures()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Crop_Feature)
    unittest.TextTestRunner(verbosity=2).run(suite)