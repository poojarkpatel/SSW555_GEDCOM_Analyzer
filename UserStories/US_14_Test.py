import unittest, os, io, sys
from UserStories.US_14 import US_14
from Programs.Base_File import Repository

class Test(unittest.TestCase):

    def test_US_14(self):
        """ Contains test cases for US_14"""
        indi_repo: Repository = Repository("../GedcomFiles/US_14.ged")

        exp = ["US14: @F1@ has more than 5 children born on same date 2005-01-01 in line number 180"]

        self.assertEqual(US_14(indi_repo._individual, indi_repo._family), exp)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)