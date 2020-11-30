import unittest
from UserStories.us_32_36 import us_32, us_36
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_us_36(self):
        """ The function helps to test us_32 function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_32_36.ged")
        expected: List = ['Line number:41 Julie /Cohen/ died recently']
        self.assertEqual(us_36(indi_repo._individual), expected)
        self.assertNotEqual(us_36(indi_repo._individual), ['John /Cohen/ died recently'])

    def test_us_32(self):
        """ this helps to test us_36 function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_32_36.ged")
        expected: List = ['Line number:21 The two or more individuals were born at the same time '
                            '@I1@:David /Cohen/',
                            'Line number:50 The two or more individuals were born at the same time '
                            '@I4@:John /Cohen/',
                            'Line number:59 The two or more individuals were born at the same time '
                            '@I5@:David /Cohen/']
        self.assertEqual(us_32(indi_repo._individual), expected)
        self.assertNotEqual(us_32(indi_repo._individual), ['@I2@:David /Cohen/ @I5@:David /Cohen/ The two or more '
                                                          'individuals were born at the same time'])

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)