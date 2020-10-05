import unittest
from US_25 import us_25
from Base_File import Repository
from typing import List


class Test(unittest.TestCase):
    """Helps to test all the functions"""

    def test_us_25(self):
        """ The function helps to test us_25 function"""
        indi_repo: Repository = Repository("US_25.ged")

        expected: List = ['The family @F2@ has multiple individuals with same name Joey /Robinson/',
                          'There are multiple people born on 1980-09-13 date in family @F1@']

        self.assertEqual(sorted(us_25(indi_repo._individual, indi_repo._family)), expected)
        self.assertNotEqual(sorted(us_25(indi_repo._individual, indi_repo._family)),
                            ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                             'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertFalse(us_25(indi_repo._individual, indi_repo._family)
                         == ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                             'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertTrue(sorted(us_25(indi_repo._individual, indi_repo._family))
                        == ['The family @F2@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1980-09-13 date in family @F1@'])
        self.assertTrue(us_25(indi_repo._individual, indi_repo._family)
                        != ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1822-01-02 date in family @F1@'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
