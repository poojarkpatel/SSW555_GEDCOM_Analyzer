import unittest
from Programs.Base_File import Repository,us_37
from typing import List

class TestRepository(unittest.TestCase):
    def test_us_37(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_37.ged")
        excepted: List = ['Living Spouse: Dhruv /Shah/ and descendant : Saddi /Shah/ on line number 115','Living Spouse: Dhiru /Shah/ and descendant : Praj /Shah/ on line number 120',
                          ' Living spouse: Riya /Patel/ and Descendant : Dhiru /Shah/ on line number 128 ','Living Spouse: Raj /Shah/ and descendant : Dhruv /Shah/ on line number 132']
        calculated: List = us_37(indi_repo._individual, indi_repo._family)
        self.assertEqual(calculated, excepted)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)