import unittest
from US_39 import US_39
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_39(self):
        """ The function helps to test US_39 function"""
        indi_repo = Repository("../GedcomFiles/US_39.ged")
        expected = ['The family id @F4@ have their marriage anniversary in the next 30 days. Line number: 419']
        self.assertEqual(US_39(indi_repo._family), expected)



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)