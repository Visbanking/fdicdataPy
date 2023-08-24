import unittest
import fdicdata
import pandas as pd

class TestFDICDataLibrary(unittest.TestCase):
    def test_dataTaxonomy_institution(self):
        expected_columns = ["Name", "Title", "Description", "Type"]

        result = fdicdata.dataTaxonomy("institution")

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)
        
        # Column isimlerinin doğru olduğunu kontrol et
        self.assertEqual(list(result.columns), expected_columns)

        # En az bir satırın olup olmadığını kontrol et
        self.assertGreaterEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()


