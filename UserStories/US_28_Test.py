import unittest
from Base_File import Repository
from typing import List
from US_28 import US_28

class TestRepository(unittest.TestCase):

    def test_US28(self):
        indi_repo: Repository = Repository("US_28.ged")
        expected:List = ['68 :- Joey /Robinson/ from FamID @F1@', '55 :- Mike /Robinson/ from FamID @F1@', '48 :- Ben /Mann/ from FamID @F1@']
        calculated:List = US_28(indi_repo)
        self.assertEqual(calculated,expected)

       
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)            
