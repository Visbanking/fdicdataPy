import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getFailures(self):
        expected_columns = ["CERT", "FAILDATE", "NAME"]

        # Test without filters
        result = fdicdata.getFailures(fields=["CERT", "FAILDATE", "NAME"])

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result.columns), expected_columns)

        # Check if any rows are returned
        self.assertGreaterEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()
