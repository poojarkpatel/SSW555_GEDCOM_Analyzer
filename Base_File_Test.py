import unittest
from Base_File import Repository
from typing import List
import datetime
from US_35 import recent_births
from US_25 import us_25


class TestRepository(unittest.TestCase):
    """Helps to test all the functions"""


    def test_recent_births(self):
        """ The function helps to test recent_births function"""
        indi_repo: Repository = Repository("US_35.ged")

        expected: List = ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday']
        self.assertEqual(recent_births(indi_repo._individual), expected)
        self.assertNotEqual(recent_births(indi_repo._individual), ['William /Robinson/ has recent birthday'])
        self.assertFalse(recent_births(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(recent_births(indi_repo._individual) == ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday'])
        self.assertTrue(recent_births(indi_repo._individual) != ['Smith /Robinson/ has recent birthday'])

    def test_us_25(self):
        """ The function helps to test us_25 function"""
        indi_repo: Repository = Repository("US_25.ged")

        expected: List = ['There are multiple people born on 1980-09-13 date in family @F1@',
                        'The family @F2@ has multiple individuals with same name Joey /Robinson/']

        self.assertEqual(us_25(indi_repo._individual, indi_repo._family), expected)
        self.assertNotEqual(us_25(indi_repo._individual, indi_repo._family),
                            ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertFalse(us_25(indi_repo._individual, indi_repo._family)
                         == ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                         'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertTrue(us_25(indi_repo._individual, indi_repo._family)
                        == ['There are multiple people born on 1980-09-13 date in family @F1@',
                        'The family @F2@ has multiple individuals with same name Joey /Robinson/'])
        self.assertTrue(us_25(indi_repo._individual, indi_repo._family)
                        != ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                        'There are multiple people born on 1822-01-02 date in family @F1@'])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
