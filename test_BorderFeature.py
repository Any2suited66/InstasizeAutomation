import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from helper_BorderExport import BordersFeatureTest
import inspect

def _by_link_text():
    pass


class Crop_Feature(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_crop(self):

        bordersFeatureTest = BordersFeatureTest(self.driver)

        bordersFeatureTest.test_borders()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Crop_Feature)
    unittest.TextTestRunner(verbosity=2).run(suite)