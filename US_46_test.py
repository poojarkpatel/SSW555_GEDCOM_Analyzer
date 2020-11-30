import unittest
from Programs.Base_File import Repository,us_46
from typing import List
import datetime

class TestRepository(unittest.TestCase):

    def test_us_46(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_46.ged")
        excepted: List = [ ' Tina /Sharma/ is married and dead on line number 30', ' Kiran /Sharma/ is married and dead on line number 51']
        calculated: List = us_46(indi_repo._individual)
        self.assertEqual(calculated, excepted)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)

