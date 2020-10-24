import unittest
from US_13 import US_13
from Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_13(self):
        """ The function helps to test US_13 function"""
        indi_repo: Repository = Repository("ssw555_input_file.ged")
        expected = {'The family id @F11@ has twins Emmy /Robinson/ and Sam /Robinson/',
                    'The family id @F11@ has twins Emmy /Robinson/ and Jil /Robinson/',
                    'The family id @F11@ has twins Jil /Robinson/ and Sam /Robinson/'}
        self.assertEqual(set([item for item in US_13(indi_repo._family, indi_repo._individual)]), expected)
    
        

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
