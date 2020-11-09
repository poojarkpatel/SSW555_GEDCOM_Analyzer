"""
Test cases for user story us01
Author: Varun Mullins
"""

import unittest
from US01 import us01
from Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story us01"""

    def test_us01(self):
        """ The function is to test us01 function"""
        indi_repo: Repository = Repository("US_01.ged")

        # The expected output
        expected = ['Birthdate on Line: 21\nUS_01: Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                    'Birthdate on Line: 156\nUS_01: Birthdate "2020-12-06" for individual id @I13@ is illeagal',
                    'On Line: 158\nUS_01: Date of death "2021-06-03" for individual id @I13@ is illeagal',
                    'Birthdate on Line: 167\nUS_01: Birthdate "2020-12-06" for individual id @I14@ is illeagal',
                    'Birthdate on Line: 177\nUS_01: Birthdate "2059-05-04" for individual id @I15@ is illeagal',
                    'On Line: 218\nUS_01: Marriage date "2025-08-04" for family id @F4@ is illeagal',
                    'On Line: 240\nUS_01: Marriage date "2090-04-05" for family id @F7@ is illeagal']

        # generating a list of the output from the function
        result = [value for value in us01(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case


if __name__ == "__main__":
    unittest.main(exit=False)
