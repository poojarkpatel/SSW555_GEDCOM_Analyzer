import unittest
from Base_File import Repository
from typing import List
import datetime
from US_35 import recent_births
from US_25 import us_25
from US_28 import US_28
from US_29 import US_29
from US_11 import US_11
from US_33 import US_33
from US_07 import US_07
from US_06 import US_06
from US01 import us01
from US04 import us04

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

        expected: List = ['The family @F2@ has multiple individuals with same name Joey /Robinson/',
                          'There are multiple people born on 1980-09-13 date in family @F1@']

        self.assertEqual(sorted(us_25(indi_repo._individual, indi_repo._family)), expected)
        self.assertNotEqual(sorted(us_25(indi_repo._individual, indi_repo._family)),
                            ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertFalse(us_25(indi_repo._individual, indi_repo._family)
                         == ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                         'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertTrue(us_25(indi_repo._individual, indi_repo._family)
                        == ['There are multiple people born on 1980-09-13 date in family @F1@',
                        'The family @F2@ has multiple individuals with same name Joey /Robinson/'])
        self.assertTrue(sorted(us_25(indi_repo._individual, indi_repo._family))
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


    def test_US_11(self):
        """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""
        indi_repo = Repository('US_11.ged')
        output = ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time']
        self.assertEqual(US_11(indi_repo), output)
        self.assertNotEqual(US_11(indi_repo), ['Ross /Galler married twice on the same time'])
        self.assertTrue(US_11(indi_repo) == ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time'])
        self.assertFalse(US_11(indi_repo) == ['Emma /Galler married twice on the same time'])
        self.assertTrue(US_11(indi_repo) != ['Ross /Galler married twice on the same time'])

    def test_US_33(self):
        """ Tests US33. checks that list all orphans. """

        indi_repo = Repository('US_33.ged')
        output = ['@I1@ Mia /Shiyani/ 17 is orphan and age is less than 18']
        self.assertEqual(US_33(indi_repo), output)
        self.assertTrue(US_33(indi_repo) == ['@I1@ Mia /Shiyani/ 17 is orphan and age is less than 18'])
        self.assertFalse(US_33(indi_repo) == ['@I1@ Yatinkumar /Shiyani/ 13 is orphan and age is less than 18'])
        self.assertTrue(US_33(indi_repo) != ['@I1@ priyanka /Shiyani/ 16 is orphan and age is less than 18'])

    def test_US_06(self):
        """ Contains test cases for US_06"""
        indi_repo: Repository = Repository("US_06.ged")

        expected = ["US_06: Katir /Bala/ Death 1822-01-03 occured prior to the divorce date 1852-07-14"]

        self.assertEqual((US_06(indi_repo._individual, indi_repo._family)), expected)
    
    def test_US_07(self):
        """ Contains test cases for US_07"""
        indi_repo: Repository = Repository("US_07.ged")

        expected = ["Tia /Ale/"]

        self.assertEqual(US_07(indi_repo._individual), expected )

    def test_us01(self):
        """ The function is to test us01 function"""
        indi_repo: Repository = Repository("US01.ged")

        # The expected output
        expected = ['US01: Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                    'US01: Birthdate "2020-12-06" for individual id @I13@ is illeagal',
                    'US01: Date of death "2021-06-03" for individual id @I13@ is illeagal',
                    'US01: Birthdate "2020-12-06" for individual id @I14@ is illeagal',
                    'US01: Birthdate "2059-05-04" for individual id @I15@ is illeagal',
                    'US01: Marriage date "2025-08-04" for family id @F4@ is illeagal',
                    'US01: Marriage date "2090-04-05" for family id @F7@ is illeagal']

        # generating a list of the output from the function
        result = [value for value in us01(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case

    def test_us04(self):
        """ The function is to test us04 function"""
        indi_repo: Repository = Repository("US04.ged")

        # The expected output
        expected = ['US04: This family id @F3@ has an illegal dates for marriage and divorce',
                    'US04: This family id @F7@ has an illegal dates for marriage and divorce']

        # generating a list of the output from the function
        result = [value for value in us04(indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['This family id @F3@ has an illegal dates for marriage and divorce']) # Negative # test case

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
