import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getSummary(self):
        expected_columns = ["ASSET", "CB_SI", "DEP", "STNAME", "YEAR"]

        result = fdicdata.getSummary(states=["California", "New York"], date_range=["2020", "2021"], fields=["DEP", "ASSET", "CB_SI"])

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
