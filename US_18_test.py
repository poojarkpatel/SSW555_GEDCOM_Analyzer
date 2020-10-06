import unittest
from US_18 import US_18
from Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_18(self):
        """ The function helps to test US_18 function"""
        indi_repo_18: Repository = Repository("ssw555_input_file.ged")
        expected = ['Individuals @I1@ and @I5@ are siblings and married.']
        self.assertEqual(US_18(indi_repo_18._family,indi_repo_18._individual), expected)
    
        

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)