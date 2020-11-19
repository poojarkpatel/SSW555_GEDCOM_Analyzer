import unittest
from UserStories.US_55_56 import US_55, US_56
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_US_55(self):
        """ The function helps to test US_55"""
        indi_repo: Repository = Repository("../GedcomFiles/US_55_56.ged")

        expected: List =['Line number 39,William /Parker Bowles/ has illegal birthdate',
                         'Line number 47,Harry /Parker Bowles/ has illegal birthdate',
                         'Line number 58,Michael /Parker Bowles/ has illegal deathdate']

        self.assertEqual(US_55(indi_repo._individual), expected)
        self.assertNotEqual(US_55(indi_repo._individual), ['Line number: 50 Anne /Parker Bowles/is below 30 and married'])

    def test_US_56(self):
        """ The function helps to test US_56"""
        indi_repo: Repository = Repository("../GedcomFiles/US_55_56.ged")

        expected: List = ['Line number: 15 Camila /Parker Bowles/is below 30 and married',
                          'Line number: 24 Andrew /Parker Bowles/is below 30 and married']

        self.assertEqual(US_56(indi_repo._individual), expected)
        self.assertNotEqual(US_56(indi_repo._individual),
                            'Line number: 25 Andrew /Parker Bowles/is below 30 and married')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
