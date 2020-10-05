import unittest
from Base_File import Repository
from typing import List
import datetime
from US_35 import recent_births
from US_25 import us_25
from US_28 import US_28
from US_29 import US_29


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

    def test_deceased(self):
        indi_repo: Repository = Repository("US_29.ged")
        excepted: List = [['Joey /Robinson/', 'Ross /Robinson/', 'Monica /Geller/',
                           'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/',
                           'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']]
        expected1: List = [['Joey /Robinson/', 'Ross /Robinson/',
                            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/',
                            'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']]
        excepted2: List = [['Joey /Robinson/', 'Ross /Robinson/', 'Monica /Geller/',
                            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/',
                            'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']
            , ['Htp /Manan/']]

        # calculated = [individual.info_individual() for individual in indi_repo._individual.values()]
        calculated = [[i for i in US_29(indi_repo)]]
        self.assertEqual(sorted(calculated), sorted(excepted))
        self.assertNotEqual(calculated, expected1)
        self.assertGreaterEqual(len(calculated), len(expected1))
        self.assertLess(len(calculated), len(excepted2))
        self.assertNotEqual(calculated, excepted2)

    def test_US28(self):
        indi_repo: Repository = Repository("US_28.ged")
        expected: List = ['68 :- Joey /Robinson/ from FamID @F1@', '55 :- Mike /Robinson/ from FamID @F1@',
                          '48 :- Ben /Mann/ from FamID @F1@']
        calculated: List = US_28(indi_repo)
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
