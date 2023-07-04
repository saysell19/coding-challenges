# Tests for the findPrime module

import unittest
import findPrime as fp

class TestPrimeFinder(unittest.TestCase):


    def test_prime_finder(self):
        """ 
        Test that the function returns the correct type
        """
        self.assertIsInstance(fp.PrimeFinder(100).prime_finder(), list)


    def test_prime_finder_values_0(self):
        """ 
        Test that the function returns the correct value
        """
        self.assertEqual(fp.PrimeFinder(0).prime_finder(), [])

    def test_prime_finder_values_19(self):
        """ 
        Test that the function returns the correct list of values given 19
        """
        self.assertEqual(fp.PrimeFinder(19).prime_finder(), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_prime_finder_values_42(self):
        """ 
        Test that the function returns the correct list of values given 42
        """
        self.assertEqual(fp.PrimeFinder(42).prime_finder(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41])

    def test_prime_finder_values_100(self):
        """ 
        Test that the function returns the correct list of values given 100
        """
        self.assertEqual(fp.PrimeFinder(100).prime_finder(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


if __name__ == '__main__':
    unittest.main()