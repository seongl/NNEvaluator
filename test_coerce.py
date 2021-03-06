import os
import numpy as np
import pandas as pd
import unittest
import zipfile
from coerce import *

class TestCoerce(unittest.TestCase):

    def setUp(self):
        """Set up tests."""
        pd.options.display.max_columns = 999
        dataZip = zipfile.ZipFile("globalterrorismdb_0718dist.csv.zip")
        self.df = pd.read_csv(dataZip.open("globalterrorismdb_0718dist.csv"), encoding = "ISO-8859-1")

    def test_string_to_number(self):
        """Test string_to_number method."""
        df = coerce_column(self.df, "nkillus", STRING_TO_NUMBER)
        self.assertEqual("float64", df["nkillus"].dtype)

    def test_float_to_int(self):
        """Test float_to_int method."""
        df = coerce_column(self.df, "nwound", FLOAT_TO_INT)
        self.assertEqual("int32", df["nwound"].dtype)

    def test_string_to_date(self):
        """Test string_to_date method."""
        df = coerce_column(self.df, "iyear", STRING_TO_DATE)
        self.assertEqual("datetime64[ns]", df["iyear"].dtype)

    def test_to_categorical(self):
        """Test to_categorical method."""
        df = coerce_column(self.df, "attacktype1_txt", TO_CATEGORICAL)
        try:
            print(df["attacktype1_txt"].tail())
            self.fail("Expected attacktype1_txt column to have been dropped from df")
        except:
            print("Original column dropped as expected.")

    def test_to_zipcode(self):
        """Test number_to_zipcode method."""
        d = {"col1": [12345, 23456, 34567, 31020301, 132, 20489, 12121, 03434]}
        df = pd.DataFrame(d)
        df = coerce_column(df, "col1", NUMBER_TO_ZIPCODE)
        print(df)
        print(df.dtypes)

if __name__ == "__main__":
    unittest.main()
