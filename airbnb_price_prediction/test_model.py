"""Test Cases for ml_model.py."""
import unittest
import os
import ml_model as mm
import numpy as np

FEATURE_COUNT = 7


class TestMlModelFunctions(unittest.TestCase):
	"""Contains test cases for various scenarios."""

	def _test_get_data(self, path, airbnb_file_name, restaurant_data_file_name):
		return mm.read_data(path, airbnb_file_name, restaurant_data_file_name)


	def _test_predict_price(self, data_instance):
		return mm.predict_price(data_instance)


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


	def test_oneHotEncode(self):
		'''Check that the oneHotEncode function can only give type error and value error'''
		current_dir_path = os.getcwd()
		airbnb_data_req, restaurant_data = self._test_get_data(current_dir_path,
															'listings.csv',
															'rest_count.csv')
		try:
			self.assertEqual(mm.oneHotEncode(airbnb_data_req, ""), False)
		except TypeError:
			self.assertTrue(True)
		except ValueError:
			self.assertTrue(True)


	def test_build_model(self):
		'''Test to check that the feature params can only be a list of values'''
		self.assertEqual(mm.build_linear_regression_model(""), False)


	def test_predict_model(self):
		'''The predicted price must be greater than 0'''
		data_instance = [0] * FEATURE_COUNT
		check = self._test_predict_price(np.array([data_instance]))
		self.assertEqual(check>0, True)


if __name__ == "__main__":
	unittest.main()
