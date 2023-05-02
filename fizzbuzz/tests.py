# Tests for the fizzbuzz module

import unittest
import fizzbuzz as hfb

class SolutionMethods(unittest.TestCase):

    def setUp(self):
        self.solution = hfb.Solution()
    
    def test_run_15(self):
        """
        Test that the function returns correct string for input of 1 and 15
        """
        self.assertEqual(self.solution.run(1, 15), "1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz" )

    def test_run_3(self):
         """
         Test that the function returns correct string for input of 1 and 3
         """
         self.assertCountEqual(self.solution.run(1, 3), "1,2,Fizz")

    def test_run_5(self):
        """
        Test that the function returns correct string for input of 1 and 5
        """
        self.assertCountEqual(self.solution.run(1, 5), "1,2,Fizz,4,Buzz" )


if __name__ == "__main__":
	unittest.main()
