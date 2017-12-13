import unittest
import pandas as pd

from cleaning import splitZip
from cleaning import rest_name
from cleaning import rest_add
from cleaning import clean_airbnb
from cleaning import clean_restraunts_geo

class TestCleaningFunctions(unittest.TestCase):

    def test_spitZip(self):
        testzip = "11426.0-1175"
        actualzip = "11426"
        self.assertEqual(splitZip(testzip), actualzip)

    def test_rest_name(self):
        comb_name = "Restaurant Name 11(Buliding Number) Address Zipcode"
        actual_name = "Restaurant Name"
        self.assertEqual(rest_name(comb_name), actual_name)

    def test_add(self):
        row = pd.DataFrame(columns = ['Restaurant', 'Name'])
        row.loc[0] = ["Restaurant Name 11(Buliding Number) Address Zipcode", 
                      "Restaurant Name"]
        address = " 11(Buliding Number) Address Zipcode"
        add = row.apply(rest_add,axis=1)[0]
        self.assertEqual(add, address)

    def test_clean_airbnb(self):
        final_shape = (36987, 17)
        fileDetails = pd.read_csv("./Data/listings.csv")
        final_df = clean_airbnb(fileDetails)
        self.assertEqual(final_df.shape, final_shape)

    def test_clean_restaurants_go(self):
        final_shape = (24941, 6)
        fileDetails = pd.read_csv(
            "./Data/NYC Restaurants Geocoded - Sheet1.csv")
        final_df = clean_restraunts_geo(fileDetails)
        self.assertEqual(final_df.shape, final_shape)


if __name__=="__main__":
    unittest.main()
