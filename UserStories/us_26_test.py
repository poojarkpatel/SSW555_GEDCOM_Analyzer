import unittest
from Programs.Base_File import Repository,us_26
from typing import List
import datetime

class TestRepository(unittest.TestCase):

    def test_us_26(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_26.ged")
        excepted: List = ['Individual in family:@F1@ is on line number 148', 'Individual in family:@F1@ is on line number 148', 'Individual in family:@F1@ is on line number 148',
                          'Individual in family:@F3@ is on line number 164','Individual in family:@F2@ is on line number 157','Individual in family:@F4@ is on line number 173']
        calculated: List = us_26(indi_repo._individual,indi_repo._family)
        self.assertEqual(calculated, excepted)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)