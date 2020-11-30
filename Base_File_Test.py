""" File that contains all the test cases. """
import unittest
from typing import List
import datetime

from Programs.Base_File import Repository

# Importing all the user stories.
from UserStories.US_01 import US_01
from UserStories.US_04 import US_04
from UserStories.US_06 import US_06
from UserStories.US_07 import US_07
from UserStories.US_11 import US_11
from UserStories.US_13 import US_13
from UserStories.US_17 import US_17
from UserStories.US_18 import US_18
from UserStories.US_23 import US_23
from UserStories.US_25 import US_25
from UserStories.US_28 import US_28
from UserStories.US_29 import US_29
from UserStories.US_33 import US_33
from UserStories.US_35 import US_35
from UserStories.US_30 import us_30
from UserStories.US_26 import us_26
from UserStories.US_34 import us_34
from UserStories.US_37 import us_37

class TestRepository(unittest.TestCase):
    """ Class that contains all the test cases. """
    def __init__(self, *args, **kwargs):
        """ Function that initializes class variable repository. """
        super(TestRepository, self).__init__(*args, **kwargs)
        # Creating an object of class Repository that will contains both individual and family dictionaries.
        # Pass the path of your GEDCOM file as a parameter below.
        self.repository = Repository('../GedcomFiles/ssw555_input_file.ged')

    def test_US_01(self):
        """ The function is to test US_01 function"""
        repository = Repository('../GedcomFiles/US_01.ged')
        # The expected output
        expected = ['US_01: Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                    'US_01: Birthdate "2020-12-06" for individual id @I13@ is illeagal',
                    'US_01: Date of death "2021-06-03" for individual id @I13@ is illeagal',
                    'US_01: Birthdate "2020-12-06" for individual id @I14@ is illeagal',
                    'US_01: Birthdate "2059-05-04" for individual id @I15@ is illeagal',
                    'US_01: Marriage date "2025-08-04" for family id @F4@ is illeagal',
                    'US_01: Marriage date "2090-04-05" for family id @F7@ is illeagal']

        # generating a list of the output from the function
        result = [value for value in US_01(repository._individual, repository._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case

    def test_US_04(self):
        """ The function is to test US_04 function"""
        repository = Repository('../GedcomFiles/US_04.ged')
        # The expected output
        expected = ['US_04: This family id @F3@ has an illegal dates for marriage and divorce',
                    'US_04: This family id @F7@ has an illegal dates for marriage and divorce']

        # generating a list of the output from the function
        result = [value for value in US_04(repository._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['This family id @F3@ has an illegal dates for marriage and divorce']) # Negative # test case

    def test_US_06(self):
        """ Contains test cases for US_06"""
        repository = Repository('../GedcomFiles/US_06.ged')
        expected = ["US_06: Katir /Bala/ Death 1822-01-03 occured prior to the divorce date 1852-07-14"]

        self.assertEqual((US_06(repository._individual, repository._family)), expected)

    def test_US_07(self):
        """ Contains test cases for US_07"""
        repository = Repository('../GedcomFiles/US_07.ged')
        expected = ["Tia /Ale/"]

        self.assertEqual(US_07(repository._individual), expected)

    def test_US_11(self):
        """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""
        repository = Repository('../GedcomFiles/US_11.ged')
        output = ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time']
        self.assertEqual(US_11(repository), output)
        self.assertNotEqual(US_11(repository), ['Ross /Galler married twice on the same time'])
        self.assertTrue(US_11(repository) == ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time'])
        self.assertFalse(US_11(repository) == ['Emma /Galler married twice on the same time'])
        self.assertTrue(US_11(repository) != ['Ross /Galler married twice on the same time'])

    def test_US_13(self):
        """ The function helps to test US_13 function"""
        expected = {'The family id @F11@ has twins Emmy /Robinson/ and Sam /Robinson/',
                    'The family id @F11@ has twins Emmy /Robinson/ and Jil /Robinson/',
                    'The family id @F11@ has twins Jil /Robinson/ and Sam /Robinson/'}
        self.assertEqual(set([item for item in US_13(self.repository._family, self.repository._individual)]), expected)

    def test_US_17(self):
        expected = {'Joey /Robinson/': 'Monica /Geller/'}
        actual = US_17(self.repository._family.values())
        self.assertEqual(expected, actual)

    def test_US_18(self):
        """ The function helps to test US_18 function"""
        expected = [['@I25@ and @I1@ are siblings and a couple.'], ['@I1@ and @I25@ are siblings and a couple.']]
        if US_18(self.repository._family, self.repository._individual) in expected:
            self.assertEqual("True", "True")
        else:
            self.assertEqual("False", "True")
        # self.assertEqual(US_18(self.repository_18._family, self.repository_18._individual), expected)

    def test_US_23(self):
        expected = {'Mike /Robinson/': datetime.date(2021, 7, 2)}
        actual = US_23(self.repository._individual)
        self.assertEqual(expected, actual)

    def test_US_25(self):
        """ The function helps to test US_25 function"""
        repository = Repository('../GedcomFiles/US_25.ged')
        expected: List = ['The family @F2@ has multiple individuals with same name Joey /Robinson/',
                          'There are multiple people born on 1980-09-13 date in family @F1@']

        self.assertEqual(sorted(US_25(repository._individual, repository._family)), expected)
        self.assertNotEqual(sorted(US_25(repository._individual, repository._family)),
                            ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                            'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertFalse(US_25(repository._individual, repository._family)
                         == ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                         'There are multiple people born on 1822-01-01 date in family @F1@'])
        self.assertTrue(US_25(repository._individual, repository._family)
                        == ['There are multiple people born on 1980-09-13 date in family @F1@',
                        'The family @F2@ has multiple individuals with same name Joey /Robinson/'])
        self.assertTrue(sorted(US_25(repository._individual, repository._family))
                        != ['The family @F1@ has multiple individuals with same name Joey /Robinson/',
                        'There are multiple people born on 1822-01-02 date in family @F1@'])

    def test_US28(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_28.ged")
        expected:List = ['68 :- Joey /Robinson/ from FamID @F1@ with individual id @I1@ is on line number 14',
        '55 :- Mike /Robinson/ from FamID @F1@ with individual id @I5@ is on line number 58',
        '48 :- Ben /Mann/ from FamID @F1@ with individual id @I4@ is on line number 47']
        calculated:List = US_28(indi_repo, indi_repo._individual)
        self.assertEqual(calculated,expected)

    def test_US_33(self):
        """ Tests US33. checks that list all orphans. """
        repository = Repository('../GedcomFiles/US_33.ged')
        output = ['@I1@ Mia /Shiyani/ has age 17 and is orphan']
        self.assertEqual(US_33(repository), output)
        self.assertTrue(US_33(repository) == output)
        self.assertFalse(US_33(repository) == ['@I1@ Yatinkumar /Shiyani/ 13 is orphan and age is less than 18'])
        self.assertTrue(US_33(repository) != ['@I1@ priyanka /Shiyani/ 16 is orphan and age is less than 18'])

    def test_US_35(self):
        """ The function helps to test US_35 function """
        repository = Repository('../GedcomFiles/US_35.ged')
        expected: List = ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday']
        self.assertEqual(US_35(repository._individual), expected)
        self.assertNotEqual(US_35(repository._individual), ['William /Robinson/ has recent birthday'])
        self.assertFalse(US_35(repository._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(US_35(repository._individual) == ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday'])
        self.assertTrue(US_35(repository._individual) != ['Smith /Robinson/ has recent birthday'])

    def test_deceased(self):
            indi_repo: Repository = Repository("../GedcomFiles/US_29.ged")
            excepted: List=[['Joey /Robinson/ on line number 21', 'Ross /Robinson/ on line number 32',
                             'Monica /Geller/ on line number 43','Ben /Mann/ on line number 54', 'Mike /Robinson/ on line number 65', 'Rachel /Green/ on line number 78', 'Ema /Mosbi/ on line number 89',
                             'William /Robinson/ on line number 100', 'Max /Robinson/ on line number 111', 'Dora /Robinson/ on line number 123', 'Jimmy /Smith/ on line number 144']]
            #calculated = [individual.info_individual() for individual in indi_repo._individual.values()]
            calculated=[[i for i in US_29(indi_repo)]]
            self.assertEqual(sorted(calculated),sorted(excepted))

    def test_us_26(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_26.ged")
        excepted: List = ['Individual in family:@F1@ is on line number 148', 'Individual in family:@F1@ is on line number 148', 'Individual in family:@F1@ is on line number 148',
                          'Individual in family:@F3@ is on line number 164','Individual in family:@F2@ is on line number 157','Individual in family:@F4@ is on line number 173']
        calculated: List = us_26(indi_repo._individual,indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_us_30(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_30.ged")
        excepted: List = [' Seema /Sharma/ is married and alive on line number 32',
                          ' Poonam /Sharma/ is married and alive on line number 41',
                          ' Snehal /Sharma/ is married and alive on line number 51',
                          ' Renu /Sharma/ is married and alive on line number 72']
        calculated: List = us_30(indi_repo._individual)
        self.assertEqual(calculated, excepted)

    def test_us_34(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_34.ged")
        excepted: List = ['Rahul /Sharma/,70 and Pinal /Sharma/ ,22  are the couples who were married when the older spouse was more than as twice as old as the younger spouse on line number 52']
        calculated: List = us_34(indi_repo._individual,indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_us_37(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_37.ged")
        excepted: List = ['Living Spouse: Dhruv /Shah/ and descendant : Saddi /Shah/ on line number 115','Living Spouse: Dhiru /Shah/ and descendant : Praj /Shah/ on line number 120',
                          ' Living spouse: Riya /Patel/ and Descendant : Dhiru /Shah/ on line number 128 ','Living Spouse: Raj /Shah/ and descendant : Dhruv /Shah/ on line number 132']
        calculated: List = us_37(indi_repo._individual, indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_us_46(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_46.ged")
        excepted: List = [ ' Tina /Sharma/ is married and dead on line number 30', ' Kiran /Sharma/ is married and dead on line number 51']
        calculated: List = us_46(indi_repo._individual)
        self.assertEqual(calculated, excepted)

    def test_us_45(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_45.ged")
        excepted: List = ['Rahul /Sharma/ on line number 21', 'Riya /Sharma/ on line number 41']
        calculated = [i for i in us_45(indi_repo)]
        self.assertEqual(calculated, excepted)


if __name__ == "__main__":
    """ Runs all the tests created above. """
    unittest.main(exit=False, verbosity=2)
