import unittest
from UserStories.US_35 import US_35
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_35(self):
        """ The function helps to test recent_births function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_35.ged")

        expected: List = ['Line number:39  Emmy /Robinson/ has recent birthday',
                          'Line number:48  Jil /Robinson/ has recent birthday',
                          'Line number:57  Sam /Robinson/ has recent birthday']

        self.assertEqual(US_35(indi_repo._individual), expected)
        self.assertNotEqual(US_35(indi_repo._individual), ['William /Robinson/ has recent birthday'])
        self.assertFalse(US_35(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(US_35(indi_repo._individual) == ['Line number:39  Emmy /Robinson/ has recent birthday',
                                                         'Line number:48  Jil /Robinson/ has recent birthday',
                                                         'Line number:57  Sam /Robinson/ has recent birthday'])
        self.assertTrue(US_35(indi_repo._individual) != ['Smith /Robinson/ has recent birthday'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
