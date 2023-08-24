import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_getHistory(self):
        expected_columns = ["CERT", "INSTNAME", "PCITY", "PSTALP", "PZIP5"]

        result_cert = fdicdata.getHistory(CERT_or_NAME=3850, fields=["INSTNAME", "CERT", "PCITY", "PSTALP", "PZIP5"], CERT=True, limit=10)

        self.assertIsNotNone(result_cert)
        self.assertIsInstance(result_cert, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result_cert.columns), expected_columns)

        result_name = fdicdata.getHistory(CERT_or_NAME="Example Bank", fields=["INSTNAME", "CERT", "PCITY", "PSTALP", "PZIP5"], CERT=False, limit=10)

        self.assertIsNotNone(result_name)
        self.assertIsInstance(result_name, pd.DataFrame)

        # Check column names
        self.assertEqual(list(result_name.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
