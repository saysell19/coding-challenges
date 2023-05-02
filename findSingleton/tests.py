# Tests for the findSingleton module

import unittest
import studentSingelton as findSingleton


class TestFindSingleton(unittest.TestCase):

    def setUp(self):
        self.test_team = findSingleton.Solution()

    def test_run_short(self):
        self.assertEqual(self.test_team.run([1, 2, 3, 4, 5, 1, 2, 3, 4]), '5')

    def test_run_long(self):
        self.assertEqual(self.test_team.run([1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10]), '5')

    @unittest.expectedFailure
    def test_run_empty(self):
        self.assertEqual(self.test_team.run([]), 'None')


if __name__ == '__main__':
    unittest.main()

