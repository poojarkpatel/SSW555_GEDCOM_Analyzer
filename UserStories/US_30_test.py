import unittest
from Programs.Base_File import Repository,us_30
from typing import List
import datetime

class TestRepository(unittest.TestCase):

    def test_us_30(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_30.ged")
        excepted: List = [' Seema /Sharma/ is married and alive on line number 32', ' Poonam /Sharma/ is married and alive on line number 41', ' Snehal /Sharma/ is married and alive on line number 51',
                          ' Renu /Sharma/ is married and alive on line number 72']
        calculated:List = us_30(indi_repo._individual)
        self.assertEqual(calculated, excepted)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)