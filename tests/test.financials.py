import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getFinancials(self):
        expected_columns = ["ASSET", "DEP", "IDRSSD", "DATE"]

        # Test without date range
        result = fdicdata.getFinancials(IDRSSD_or_CERT=37, metrics=["ASSET", "DEP"])

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result.columns), expected_columns)

        # Test with date range
        result_with_date_range = fdicdata.getFinancials(IDRSSD_or_CERT=37, metrics=["ASSET", "DEP"], date_range=["20230101", "20231231"])

        self.assertIsNotNone(result_with_date_range)
        self.assertIsInstance(result_with_date_range, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result_with_date_range.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
