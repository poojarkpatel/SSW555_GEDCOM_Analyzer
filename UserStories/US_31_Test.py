import unittest
from UserStories.US_31 import US_31
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_31(self):
        """ The function helps to test US_31"""
        indi_repo: Repository = Repository("../GedcomFiles/US_31.ged")

        expected: List = ['Line number: 33 Charles /Windsor/is over 30 and still not married']

        self.assertEqual(US_31(indi_repo._individual), expected)
        self.assertNotEqual(US_31(indi_repo._individual), ['William /Robinson/ has recent birthday'])
        self.assertFalse(US_31(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(US_31(indi_repo._individual) == ['Line number: 33 Charles /Windsor/is over 30 and still '
                                                         'not married'])
        self.assertTrue(US_31(indi_repo._individual) != ['Smith /Robinson/ has recent birthday'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)