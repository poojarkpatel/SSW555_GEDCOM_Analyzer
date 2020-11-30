import unittest, os, io, sys
from UserStories.US_54 import US_54
from Programs.Base_File import Repository

class Test(unittest.TestCase):

    def test_US_54(self):
        """ Contains test cases for US_54"""
        indi_repo: Repository = Repository("../GedcomFiles/US_53.ged")

        exp = ["US_54: Katir /Bala/ with @I3@ is younger than child Pia /Ale/ in line number 180 "]

        self.assertEqual(US_54(indi_repo._individual, indi_repo._family), exp)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)