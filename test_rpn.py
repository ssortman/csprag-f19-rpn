import unittest
import rpn

class TestBasics(unittest.TestCase): 
	def test_add(self):
		result = rpn.calculate('1 1 + ')
		self.assertEqual(2, result)
	def test_pow(self):
		result = rpn.calculate('2 3 ^ ')
		self.assertEqual(8, result)
