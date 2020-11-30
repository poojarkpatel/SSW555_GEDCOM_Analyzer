import unittest
from US_51 import US_51
from Programs.Base_File import Repository
from typing import List

class Test(unittest.TestCase):
    """This function helps to test all the functions"""

    def test_US_51(self):
        """ The function helps to test US_51 function"""
        indi_repo = Repository("../GedcomFiles/US_51.ged")
        expected = ['The family id @F4@ have their marriage anniversary in the next 2 months. Line number: 419']
        self.assertEqual(US_51(indi_repo._family), expected)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)