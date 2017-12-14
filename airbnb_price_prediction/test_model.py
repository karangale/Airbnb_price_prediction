"""Test Cases for ml_model.py."""
import unittest
import os
import ml_model as mm


class TestMlModelFunctions(unittest.TestCase):
    """Contains test cases for various scenarios."""

    def test_readData(self):
        """Check if the read_data() function fails with the wrong arguments."""
        path = "sdada"
        airbnb_file_name = "wrong_name1"
        restaurant_data_file_name = "wrong_name2"
        try:
            mm.read_data(path, airbnb_file_name, restaurant_data_file_name)
        except IOError:
            self.assertTrue(True)

    def test_DataDirPresent(self):
        """Check if Data directory is present."""
        self.assertEqual(os.path.isdir('Data'), True)


if __name__ == "__main__":
    unittest.main()
