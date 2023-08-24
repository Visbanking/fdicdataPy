import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getInstitution(self):
        expected_columns = ["CITY", "IDRSSD", "NAME", "DATE"]

        # Test with name parameter
        result_with_name = fdicdata.getInstitution(name="Bank of America", fields=["CITY", "IDRSSD", "NAME", "REPDTE"])

        self.assertIsNotNone(result_with_name)
        self.assertIsInstance(result_with_name, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result_with_name.columns), expected_columns)

        # Test with IDRSSD_or_CERT parameter
        result_with_idrssd = fdicdata.getInstitution(IDRSSD_or_CERT=480228, fields=["CITY", "IDRSSD", "NAME", "REPDTE"], IDRSSD=True)

        self.assertIsNotNone(result_with_idrssd)
        self.assertIsInstance(result_with_idrssd, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result_with_idrssd.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
