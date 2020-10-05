import unittest
from US_35 import recent_births
from Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_recent_births(self):
        """ The function helps to test recent_births function"""
        indi_repo: Repository = Repository("/Users/poojapatel/Downloads/US_35.ged")

        expected: List = ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday',
                          'Sam /Robinson/ has recent birthday']
        self.assertEqual(recent_births(indi_repo._individual), expected)
        self.assertNotEqual(recent_births(indi_repo._individual), ['William /Robinson/ has recent birthday'])
        self.assertFalse(recent_births(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(recent_births(indi_repo._individual) == ['Emmy /Robinson/ has recent birthday',
                                                                 'Jil /Robinson/ has recent birthday',
                                                                 'Sam /Robinson/ has recent birthday'])
        self.assertTrue(recent_births(indi_repo._individual) != ['Smith /Robinson/ has recent birthday'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
