import unittest
from CoastFilterExportTest import CoastFilterTestCase

from AthensFilterExport import AthensFilterExportTest

coastFilter = unittest.TestLoader().loadTestsFromTestCase(CoastFilterTestCase)
athensFilter = unittest.TestLoader().loadTestsFromTestCase(AthensFilterExportTest)

test_suite = unittest.TestSuite([coastFilter, athensFilter])

unittest.TextTestRunner(verbosity=2).run(test_suite)
