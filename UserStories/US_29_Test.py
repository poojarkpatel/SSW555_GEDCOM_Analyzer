import unittest
from Programs.Base_File import Repository,US_29
from typing import List
import datetime

class TestRepository(unittest.TestCase):
 
    def test_deceased(self):
            indi_repo: Repository = Repository("../GedcomFiles/US_29.ged")
            excepted: List=[['Joey /Robinson/ on line number 21', 'Ross /Robinson/ on line number 32',
                             'Monica /Geller/ on line number 43','Ben /Mann/ on line number 54', 'Mike /Robinson/ on line number 65', 'Rachel /Green/ on line number 78', 'Ema /Mosbi/ on line number 89',
                             'William /Robinson/ on line number 100', 'Max /Robinson/ on line number 111', 'Dora /Robinson/ on line number 123', 'Jimmy /Smith/ on line number 144']]
            #calculated = [individual.info_individual() for individual in indi_repo._individual.values()]
            calculated=[[i for i in US_29(indi_repo)]]
            self.assertEqual(sorted(calculated),sorted(excepted))

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)            
