import unittest
from Programs.Base_File import Repository,us_34
from typing import List

class TestRepository(unittest.TestCase):
    def test_us_34(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_34.ged")
        excepted: List = ['Rahul /Sharma/,70 and Pinal /Sharma/ ,22  are the couples who were married when the older spouse was more than as twice as old as the younger spouse on line number 52']
        calculated: List = us_34(indi_repo._individual,indi_repo._family)
        self.assertEqual(calculated, excepted)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)