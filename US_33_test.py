"""
Author:Priyankaben Shiyani
SSW 555 Agile Methods for Software Development 
Purpose: Testing for user story 11
"""
import unittest, os, io, sys
from Base_File import Repository, Individual, Family
from US_33 import US_33

class Test_US_33(unittest.TestCase):
    """ Tests US33. checks that list all orphans. """

    def test_US_33(self):
        """ Tests US33. checks that list all orphans. """

        indi_repo = Repository('US_33.ged')
        output = ['@I1@ Mia /Shiyani/ 17 is orphan and age is less than 18']
        self.assertEqual(US_33(indi_repo), output)
        self.assertTrue(US_33(indi_repo) == ['@I1@ Mia /Shiyani/ 17 is orphan and age is less than 18'])
        self.assertFalse(US_33(indi_repo) == ['@I1@ Yatinkumar /Shiyani/ 13 is orphan and age is less than 18'])
        self.assertTrue(US_33(indi_repo) != ['@I1@ priyanka /Shiyani/ 16 is orphan and age is less than 18'])

if __name__ == "__main__":
    unittest.main(exit=False)
