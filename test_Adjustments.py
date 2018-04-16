import unittest
from DriverBuilder7zero import DriverBuilderAndroid
from AdjustmentsHelper import AdjustmentsHelper
import inspect

def _by_link_text():
    pass


class AdjustmentsTest(unittest.TestCase):
    # Class to run tests on exporting photos to Instagram

    driver_builder = DriverBuilderAndroid()
    driver = driver_builder.driver

    def test_adjustments(self):

        adjustmentsHelper = AdjustmentsHelper(self.driver)

        adjustmentsHelper.allAdjustments()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AdjustmentsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
