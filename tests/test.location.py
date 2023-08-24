import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getLocation(self):
        expected_columns = ["CERT", "CITY", "ESTYMD", "MAINOFF", "NAME", "ZIP"]

        result = fdicdata.getLocation(cert=3850, fields=["CERT", "CITY", "ESTYMD", "MAINOFF", "NAME", "ZIP"])

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
