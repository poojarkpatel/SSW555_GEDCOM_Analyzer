import unittest, os, io, sys
from UserStories.US_53 import US_53
from Programs.Base_File import Repository

class Test(unittest.TestCase):

    def test_US_53(self):
        """ Contains test cases for US_53"""
        indi_repo: Repository = Repository("../GedcomFiles/US_53.ged")

        exp = ["US_53: Husband Katir /Bala/ with @I2@ has the same name as wife Katir /Bala/ with @I3@ in line number 180 "]

        self.assertEqual(US_53(indi_repo._individual, indi_repo._family), exp)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)