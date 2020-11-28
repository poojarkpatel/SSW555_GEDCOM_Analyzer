import unittest
from Programs.Base_File import Repository,us_45
from typing import List
import datetime

class TestRepository(unittest.TestCase):

    def test_us_45(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_45.ged")
        excepted: List = ['Rahul /Sharma/ on line number 21', 'Riya /Sharma/ on line number 41']
        calculated = [i for i in us_45(indi_repo)]
        self.assertEqual(calculated, excepted)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)