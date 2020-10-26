import unittest, os, io, sys
from UserStories.US_15 import US_15
from Programs.Base_File import Repository

class Test(unittest.TestCase):

    def test_US_15(self):
        """ Contains test cases for US_15"""
        indi_repo: Repository = Repository("../GedcomFiles/US_15.ged")

        expected = ["US:15 Family id:@F1@ has 15 or more children on line number 180"]

        self.assertEqual(US_15(indi_repo._family), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)