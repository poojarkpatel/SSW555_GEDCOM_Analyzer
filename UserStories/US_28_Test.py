import unittest
from Programs.Base_File import Repository,US_28
from typing import List

class TestRepository(unittest.TestCase):

    def test_US28(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_28.ged")
        expected:List = ['68 :- Joey /Robinson/ from FamID @F1@ with individual id @I1@ is on line number 14',
        '55 :- Mike /Robinson/ from FamID @F1@ with individual id @I5@ is on line number 58',
        '48 :- Ben /Mann/ from FamID @F1@ with individual id @I4@ is on line number 47']
        calculated:List = US_28(indi_repo, indi_repo._individual)
        self.assertEqual(calculated,expected)

       
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)            
