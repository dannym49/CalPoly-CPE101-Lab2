import unittest
from math import * 
from funcs import *

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(f(3), 69)
      
   def test_f_2(self):
      # Add code here. REMOVE PASS
      self.assertEqual(f(10), 720)

   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertRaises(ZeroDivisionError, g, 0, 3)
   
   # Add five more tests...

   def test_g_2(self):
      self.assertAlmostEqual(g(5, 8), 5.9333333)
   
   def test_hyp_1(self):
      self.assertAlmostEqual(hypotenuse(3,4), 5.0)

   def test_hyp_2(self):
      self.assertAlmostEqual(hypotenuse(7, 9), 11.401754250)

   def test_pos_1(self):
      self.assertTrue(is_positive(3))

   def test_pos_2(self):
      self.assertFalse(is_positive(-5))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

