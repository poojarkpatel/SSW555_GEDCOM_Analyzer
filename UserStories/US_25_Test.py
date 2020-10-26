import unittest
from UserStories.US_25 import US_25
from Programs.Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_us_25(self):
        """ The function helps to test us_25 function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_25.ged")

        expected: List = ['Line number 61,70 There are multiple individual born with same name: Joey '
                          '/Robinson/ ',
                          'Line number 67,76 There are multiple individual born on same date: '
                          '1997-11-08']

        self.assertEqual(US_25(indi_repo._individual, indi_repo._family), expected)
        self.assertNotEqual(sorted(US_25(indi_repo._individual, indi_repo._family)),
                            ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                             'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertFalse(US_25(indi_repo._individual, indi_repo._family)
                         == ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                             'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertTrue(US_25(indi_repo._individual, indi_repo._family)
                        != ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1822-01-02 date in family @F1@'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
