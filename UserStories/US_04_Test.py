"""
Test cases for user story us04
Author: Varun Mullins
"""

import unittest
from US04 import us04
from Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story us04"""
    def test_us04(self):
        """ The function is to test us04 function"""
        indi_repo: Repository = Repository("US04.ged")

        # The expected output
        expected = ['US04: This family id @F3@ has an illegal dates for marriage and divorce',
                    'US04: This family id @F7@ has an illegal dates for marriage and divorce']

        # generating a list of the output from the function
        result = [value for value in us04(indi_repo.family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['This family id @F3@ has an illegal dates for marriage and divorce']) # Negative # test case

if __name__ == "__main__":
    unittest.main(exit=False)