import unittest
from UserStories.US_38 import US_38
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_38(self):
        """ The function helps to test upcoming birthdates"""
        indi_repo: Repository = Repository("../GedcomFiles/US_38.ged")

        expected: List = ['Line number 39, Emmy /Robinson/ has upcoming birthday',
                          'Line number 48, Jil /Robinson/ has upcoming birthday',
                          'Line number 57, Sam /Robinson/ has upcoming birthday']

        self.assertEqual(US_38(indi_repo._individual), expected)
        self.assertNotEqual(US_38(indi_repo._individual), ['William /Robinson/ has upcoming birthday'])
        self.assertFalse(US_38(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(US_38(indi_repo._individual) ==['Line number 39, Emmy /Robinson/ has upcoming birthday',
                                                        'Line number 48, Jil /Robinson/ has upcoming birthday',
                                                        'Line number 57, Sam /Robinson/ has upcoming birthday'])
        self.assertTrue(US_38(indi_repo._individual) != ['Smith /Robinson/ has upcoming birthday'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
