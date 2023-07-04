# Tests for the xthInOrder module

import unittest
import xth_in_order as xio

class TestXthInOrder(unittest.TestCase):

    # Set up the unordered list to be used in the tests
    def setUp(self):
        self.list = [-13, 41, -31, -23, -1, 1, -29, 26, 31, -26, 26, 37, 25, -36, 7, -21, 23, -1, 37, -6]

    def test_xth_in_order(self):
        """
        Test that the function returns the correct type
        """
        self.assertIsInstance(xio.XthInOrder(2, self.list).getX(), int)

    def test_xth_in_order_values_1(self):
        """
        Test that the function returns the correct value
        """
        self.assertEqual(xio.XthInOrder(2, self.list).getX(), -31)

    def test_xth_in_order_values_2(self):
        """
        Test that the function returns the correct value
        """
        self.assertEqual(xio.XthInOrder(7, self.list).getX(), -13)

    def test_xth_in_order_values_3(self):
        """
        Test that the function returns the correct value
        """
        self.assertEqual(xio.XthInOrder(8, self.list).getX(), -6)
    
    def test_xth_in_order_values_4(self):
        """
        Test a number that is Out of Range
        """
        self.assertEqual(xio.XthInOrder(21, self.list).getX(), 0)


if __name__ == '__main__':
    unittest.main()




