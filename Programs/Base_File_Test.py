""" File that contains all the test cases. """
import unittest
from typing import List
import datetime

from Programs.Repository import Repository

# Importing all the user stories.
from UserStories.US_01 import US_01
from UserStories.US_2_3 import US_2, US_3
from UserStories.US_04 import US_04
from UserStories.US_05 import US_05
from UserStories.US_06 import US_06
from UserStories.US_07 import US_07
from UserStories.US_08 import US_08
from UserStories.US_09 import US_09
from UserStories.US_10 import US_10
from UserStories.US_11 import US_11
from UserStories.US_12 import US_12
from UserStories.US_13 import US_13
from UserStories.US_14 import US_14
from UserStories.US_15 import US_15
from UserStories.US_16 import US_16
from UserStories.US_17 import US_17
from UserStories.US_18 import US_18
from UserStories.US_19 import US_19
from UserStories.US_20 import US_20
from UserStories.US_21 import US_21
from UserStories.US_22 import US_22
from UserStories.US_23 import US_23
from UserStories.US_24 import US_24
from UserStories.US_25 import US_25
from UserStories.US_26 import us_26
from UserStories.US_28 import US_28
from UserStories.US_29 import US_29
from UserStories.US_30 import us_30
from UserStories.US_31 import US_31
from UserStories.us_32_36 import us_32, us_36
from UserStories.US_33 import US_33
from UserStories.US_34 import us_34
from UserStories.US_35 import US_35
from UserStories.US_37 import us_37
from UserStories.US_38 import US_38
from UserStories.US_39 import US_39
from UserStories.US_47 import US_47
from UserStories.US_48 import US_48


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
        expected = ['Birthdate on Line: 21\nUS_01: Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                    'Birthdate on Line: 156\nUS_01: Birthdate "2020-12-06" for individual id @I13@ is illeagal',
                    'On Line: 158\nUS_01: Date of death "2021-06-03" for individual id @I13@ is illeagal',
                    'Birthdate on Line: 167\nUS_01: Birthdate "2020-12-06" for individual id @I14@ is illeagal',
                    'Birthdate on Line: 177\nUS_01: Birthdate "2059-05-04" for individual id @I15@ is illeagal',
                    'On Line: 218\nUS_01: Marriage date "2025-08-04" for family id @F4@ is illeagal',
                    'On Line: 240\nUS_01: Marriage date "2090-04-05" for family id @F7@ is illeagal']

        # generating a list of the output from the function
        result = [value for value in US_01(repository._individual, repository._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case

    def test_US_02(self):
        """ FUnction that tests user story 2 """
        repository = Repository("../GedcomFiles/ssw555_input_file.ged")
        expected = ['US_02 - Micheal /Mia/ birthday after marriage date on line number 604',
                    'US_02 - Mike /Robinson/ birthday after marriage date on line number 604',
                    'US_02 - Sam /Robinson/ birthday after marriage date on line number 633']
        actual = US_2(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

    def test_US_03(self):
        """ Function that tests user story 3 """
        repository = Repository("../GedcomFiles/ssw555_input_file.ged")
        expected = []
        actual = US_3(repository.get_individual())
        self.assertEqual(expected, actual)

    def test_US_04(self):
        """ The function is to test US_04 function"""
        repository = Repository('../GedcomFiles/US_04.ged')
        # The expected output
        expected = ['Marriage date Line: 209\nDivorce date Line: 211\nUS_04: This family id @F3@ has an illegal dates '
                    'for marriage and divorce',
                    'Marriage date Line: 240\nDivorce date Line: 242\nUS_04: This family id @F7@ has an illegal dates '
                    'for marriage and divorce']

        # generating a list of the output from the function
        result = [value for value in US_04(repository._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['This family id @F3@ has an illegal dates for marriage and divorce'])  # Negative # test case

    def test_US_05(self):
        """ The function is to test US_05 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ["Marriage date Line: 616\nDeath of wife date Line: 60\n"
                    "The family @F14@ has a death of wife @I4@ before the marriage date."]

        # generating a list of the output from the function
        result = [value for value in US_05(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case

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

    def test_US_08(self):
        """ The function is to test US_08 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ['Family id Line number: 506\n'
                    'The Father @I1@ is younger than his child @I4@ which is illeagal.',
                    'Family id Line number: 599\n'
                    'The Father @I31@ is younger than his child @I33@ which is illeagal.',
                    'Family id Line number: 618\n'
                    'The Father @I36@ is younger than his child @I1@ which is illeagal.',
                    'Family id Line number: 647\n'
                    'The Mother @I48@ is younger than her child @I42@ which is illeagal.',
                    'Family id Line number: 652\n'
                    'The Father @I47@ is younger than his child @I43@ which is illeagal.',
                    'Family id Line number: 657\n'
                    'The Father @I44@ is younger than his child @I45@ which is illeagal.']

        # generating a list of the output from the function
        result = [value for value in US_08(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case

    def test_us09(self):
        """ The function is to test US_09 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = {'Family id Line number: 513\n'
                    'Birth of child @I28@ is before the death of the father @I27@',
                    'Family id Line number: 513\n'
                    'Birth of child @I28@ is before the death of the mother @I2@',
                    'Family id Line number: 522\n'
                    'Birth of child @I35@ is before the death of the father @I3@',
                    'Family id Line number: 522\n'
                    'Birth of child @I35@ is before the death of the mother @I4@',
                    'Family id Line number: 522\n'
                    'Birth of child @I31@ is before the death of the father @I3@',
                    'Family id Line number: 522\n'
                    'Birth of child @I31@ is before the death of the mother @I4@'}

        # generating a list of the output from the function
        result = {value for value in US_09(indi_repo._individual, indi_repo._family)}

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case

    def test_us10(self):
        """ The function is to test US_10 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ['Family id Line number: 506\n'
                    'The husband @I1@ was younger than 14 at the time of marriage for @F1@',
                    'Family id Line number: 599\n'
                    'The husband @I31@ was younger than 14 at the time of marriage for @F13@',
                    'Family id Line number: 599\n'
                    'The wife @I32@ was younger than 14 at the time of marriage for @F13@',
                    'Family id Line number: 608\n'
                    'The husband @I1@ was younger than 14 at the time of marriage for @F14@',
                    'Family id Line number: 629\n'
                    'The husband @I1@ was younger than 14 at the time of marriage for @F20@',
                    'Family id Line number: 629\n'
                    'The wife @I25@ was younger than 14 at the time of marriage for @F20@']

        # generating a list of the output from the function
        result = [value for value in US_10(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case

    def test_US_11(self):
        """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""
        repository = Repository('../GedcomFiles/US_11.ged')
        output = ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time']
        self.assertEqual(US_11(repository), output)
        self.assertNotEqual(US_11(repository), ['Ross /Galler married twice on the same time'])
        self.assertTrue(US_11(repository) == ['Joey /BIng/married twice at the same time',
                                              'Rachel /Green/married twice at the same time'])
        self.assertFalse(US_11(repository) == ['Emma /Galler married twice on the same time'])
        self.assertTrue(US_11(repository) != ['Ross /Galler married twice on the same time'])

    def test_US_12(self):
        """ Contains test cases for US_12"""
        indi_repo: Repository = Repository("../GedcomFiles/US_12.ged")

        exp = [
            "US_12: Yatinkumar /Shiyani/ with @I27@ is 80 years or older than Mia /Shiyani/ id:{'@I28@'} in line number 398 ",
            "US_12: Priyanka /Robinson/ with @I2@ is 60 years or older than Mia /Shiyani/ id:{'@I28@'} in line number 398 "]

        self.assertEqual(US_12(indi_repo._individual, indi_repo._family), exp)

    def test_US_13(self):
        """ The function helps to test US_13 function"""
        expected = {'The family id @F11@ has twins Emmy /Robinson/ and Sam /Robinson/, Line number: 584',
                    'The family id @F11@ has twins Emmy /Robinson/ and Jil /Robinson/, Line number: 584',
                    'The family id @F11@ has twins Jil /Robinson/ and Sam /Robinson/, Line number: 584'}
        self.assertEqual(set([item for item in US_13(self.repository._family, self.repository._individual)]), expected)

    def test_US_14(self):
        """ Contains test cases for US_14"""
        indi_repo: Repository = Repository("../GedcomFiles/US_14.ged")

        exp = ["US14: @F1@ has more than 5 children born on same date 2005-01-01 in line number 180"]

        self.assertEqual(US_14(indi_repo._individual, indi_repo._family), exp)

    def test_US_17(self):
        expected = {'Joey /Robinson/': 'Monica /Geller/', 'Praj /Shah/': 'Gari /Jain/'}
        actual = US_17(self.repository._family.values())
        self.assertEqual(expected, actual)

    def test_US_18(self):
        """ The function helps to test US_18 function"""
        expected = {'@I1@ and @I25@ are siblings and a couple. Line number: 631'}
        result = {value for value in US_18(self.repository._family, self.repository._individual)}
        self.assertEqual(expected, result)

        # self.assertEqual(US_18(self.repository_18._family, self.repository_18._individual), expected)

    def test_US_19(self):
        """ Function that tests user story 19 """
        repository = Repository("../GedcomFiles/US_19.ged")
        expected = ['US_19: First cousins @I7@ and @I8@ married on line 76']
        actual = US_19(repository.get_individual(), repository.get_family())

        self.assertEqual(expected, actual)

    def test_US_20(self):
        """ The function helps to test US_20 function"""
        repository = Repository("../GedcomFiles/US_20.ged")
        expected = ["Individuals @I1@ and @I9@ are uncle/aunt and niece/nephew married on line number 324"]
        self.assertEqual(US_20(repository._family, repository._individual), expected)

    def test_US_21(self):
        """ Function that tests user story 21 """
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = ['US_21: Sam /Robinson/ gender is supposed to be female but is not on line number 269']
        actual = US_21(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

    def test_US_22(self):
        """ Function that tests user story 22 """
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = []
        actual = US_22(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

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

    def test_us_26(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_26.ged")
        excepted: List = ['Individual in family:@F1@ is on line number 148',
                          'Individual in family:@F1@ is on line number 148',
                          'Individual in family:@F1@ is on line number 148',
                          'Individual in family:@F3@ is on line number 164',
                          'Individual in family:@F2@ is on line number 157',
                          'Individual in family:@F4@ is on line number 173']
        calculated: List = us_26(indi_repo._individual, indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_US_28(self):
        repository = Repository('../GedcomFiles/US_28.ged')
        expected: List = ['68 :- Joey /Robinson/ from FamID @F1@ with individual id @I1@ is on line '
                          'number 14',
                          '55 :- Mike /Robinson/ from FamID @F1@ with individual id @I5@ is on line '
                          'number 58',
                          '48 :- Ben /Mann/ from FamID @F1@ with individual id @I4@ is on line number '
                          '47']
        calculated: List = US_28(repository.get_individual(), repository.get_family())
        self.assertEqual(calculated, expected)

    def test_us_30(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_30.ged")
        excepted: List = [' Seema /Sharma/ is married and alive on line number 32', ' Poonam /Sharma/ is married and alive on line number 41', ' Snehal /Sharma/ is married and alive on line number 51',
                          ' Renu /Sharma/ is married and alive on line number 72']
        calculated:List = us_30(indi_repo._individual)
        self.assertEqual(calculated, excepted)

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

    def test_us_32(self):
        """ this helps to test us_36 function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_32_36.ged")
        expected: List = ['Line number:21 The two or more individuals were born at the same time '
                          '@I1@:David /Cohen/',
                          'Line number:50 The two or more individuals were born at the same time '
                          '@I4@:John /Cohen/',
                          'Line number:59 The two or more individuals were born at the same time '
                          '@I5@:David /Cohen/']
        self.assertEqual(us_32(indi_repo._individual), expected)
        self.assertNotEqual(us_32(indi_repo._individual), ['@I2@:David /Cohen/ @I5@:David /Cohen/ The two or more '
                                                           'individuals were born at the same time'])

    def test_US_33(self):
        """ Tests US33. checks that list all orphans. """
        repository = Repository('../GedcomFiles/US_33.ged')
        output = ['@I1@ Mia /Shiyani/ has age 17 and is orphan']
        self.assertEqual(US_33(repository), output)
        self.assertTrue(US_33(repository) == output)
        self.assertFalse(US_33(repository) == ['@I1@ Yatinkumar /Shiyani/ 13 is orphan and age is less than 18'])
        self.assertTrue(US_33(repository) != ['@I1@ priyanka /Shiyani/ 16 is orphan and age is less than 18'])

    def test_us_34(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_34.ged")
        excepted: List = ['Rahul /Sharma/,70 and Pinal /Sharma/ ,22  are the couples who were married when the older spouse was more than as twice as old as the younger spouse on line number 52']
        calculated: List = us_34(indi_repo._individual,indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_us_36(self):
        """ The function helps to test us_32 function"""
        indi_repo: Repository = Repository("../GedcomFiles/US_32_36.ged")
        expected: List = []  # 'Line number:41 Julie /Cohen/ died recently'
        self.assertEqual(us_36(indi_repo._individual), expected)
        self.assertNotEqual(us_36(indi_repo._individual), ['John /Cohen/ died recently'])

    def test_us_37(self):
        indi_repo: Repository = Repository("../GedcomFiles/US_37.ged")
        excepted: List = ['Living Spouse: Dhruv /Shah/ and descendant : Saddi /Shah/ on line number 115','Living Spouse: Dhiru /Shah/ and descendant : Praj /Shah/ on line number 120',
                          ' Living spouse: Riya /Patel/ and Descendant : Dhiru /Shah/ on line number 128 ','Living Spouse: Raj /Shah/ and descendant : Dhruv /Shah/ on line number 132']
        calculated: List = us_37(indi_repo._individual, indi_repo._family)
        self.assertEqual(calculated, excepted)

    def test_US_38(self):
        """ The function helps to test upcoming birthdates"""
        indi_repo: Repository = Repository("../GedcomFiles/US_38.ged")

        expected: List = ['Line number 39, Emmy /Robinson/ has upcoming birthday',
                          'Line number 48, Jil /Robinson/ has upcoming birthday',
                          'Line number 57, Sam /Robinson/ has upcoming birthday']

        self.assertEqual(US_38(indi_repo._individual), expected)
        self.assertNotEqual(US_38(indi_repo._individual), ['William /Robinson/ has upcoming birthday'])
        self.assertFalse(US_38(indi_repo._individual) == ['Jim /Robinson/ has recent birthday'])
        self.assertTrue(US_38(indi_repo._individual) == ['Line number 39, Emmy /Robinson/ has upcoming birthday',
                                                         'Line number 48, Jil /Robinson/ has upcoming birthday',
                                                         'Line number 57, Sam /Robinson/ has upcoming birthday'])
        self.assertTrue(US_38(indi_repo._individual) != ['Smith /Robinson/ has upcoming birthday'])

    def test_US_39(self):
        """ The function helps to test US_39 function"""
        indi_repo = Repository("../GedcomFiles/US_39.ged")
        expected = ['The family id @F4@ have their marriage anniversary in the next 30 days. Line number: 419']
        self.assertEqual(US_39(indi_repo._family), expected)

    def test_US_41(self):
        repository = Repository('../GedcomFiles/ssw555_input_file.ged')
        individual = repository.get_individual()

        self.assertEqual(individual['@I2@']._birth_date, datetime.datetime.strptime("1 JAN 1830", '%d %b %Y').date())

    def test_US_42(self):
        """ Function that tests user story 42 """
        repository = Repository('../GedcomFiles/ssw555_input_file.ged')
        individual = repository.get_individual()

        self.assertEqual(individual['@I1@']._birth_date, datetime.datetime.strptime("1 JAN 1850", '%d %b %Y').date())

    # def test_US_35(self):
    #     """ The function helps to test US_35 function """
    #     repository = Repository('../GedcomFiles/US_35.ged')
    #     expected: List = ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday']
    #     self.assertEqual(US_35(repository._individual), expected)
    #     self.assertNotEqual(US_35(repository._individual), ['William /Robinson/ has recent birthday'])
    #     self.assertFalse(US_35(repository._individual) == ['Jim /Robinson/ has recent birthday'])
    #     self.assertTrue(US_35(repository._individual) == ['Emmy /Robinson/ has recent birthday', 'Jil /Robinson/ has recent birthday', 'Sam /Robinson/ has recent birthday'])
    #     self.assertTrue(US_35(repository._individual) != ['Smith /Robinson/ has recent birthday'])

    def test_US_35(self):
        """ The function helps to test US_35 function """
        repository = Repository('../GedcomFiles/US_35.ged')
        expected: List = []  # 'Jil /Robinson/ has recent birthday'

        self.assertEqual(US_35(repository._individual), expected)
        self.assertNotEqual(US_35(repository._individual), ['William /Robinson/ has recent birthday'])
        self.assertTrue(US_35(repository._individual) != ['Smith /Robinson/ has recent birthday'])

    def test_deceased(self):
        # User story 29
        repository = Repository('../GedcomFiles/US_29.ged')
        excepted: List = [['Joey /Robinson/ on line number 21', 'Ross /Robinson/ on line number 32',
                           'Monica /Geller/ on line number 43',
                           'Ben /Mann/ on line number 54', 'Mike /Robinson/ on line number 65',
                           'Rachel /Green/ on line number 78', 'Ema /Mosbi/ on line number 89',
                           'William /Robinson/ on line number 100',
                           'Max /Robinson/ on line number 111', 'Dora /Robinson/ on line number 123',
                           'Jimmy /Smith/ on line number 144']]
        expected1: List = [['Joey /Robinson/', 'Ross /Robinson/',
                            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/',
                            'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']]
        excepted2: List = [['Joey /Robinson/', 'Ross /Robinson/', 'Monica /Geller/',
                            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/',
                            'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/'], ['Htp /Manan/']]

        # calculated = [individual.info_individual() for individual in self.repository._individual.values()]
        calculated = [[i for i in US_29(repository)]]
        self.assertEqual(sorted(calculated), sorted(excepted))
        self.assertNotEqual(calculated, expected1)
        self.assertGreaterEqual(len(calculated), len(expected1))
        self.assertLess(len(calculated), len(excepted2))
        self.assertNotEqual(calculated, excepted2)

    def test_US_16(self):
        """ Contains test cases for US_16"""
        indi_repo: Repository = Repository("../GedcomFiles/US_16.ged")

        expected = [
            'US_16: Family id @F15@ with father Ribu /Watson/ and son Joey /Robinson/ have different last names on line number 503',
            'US_16: Family id @F15@ with father Ribu /Watson/ and son Sam /Robinson/ have different last names on line number 503',
            'US_16: Family id @F2@ with father Ross /Robinson/ and son Ben /Mann/ have different last names on line number 407',
            'US_16: Family id @F2@ with father Ross /Robinson/ and son Ginger /Ale/ have different last names on line number 407']

        self.assertEqual(US_16(indi_repo._individual, indi_repo._family), expected)

    def test_US_15(self):
        """ Contains test cases for US_15"""
        indi_repo: Repository = Repository("../GedcomFiles/US_15.ged")

        expected = ["US:15 Family id:@F1@ has 15 or more children on line number 180"]

        self.assertEqual(US_15(indi_repo._family), expected)

    def test_US_47(self):
        """ The function is to test US_47 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ['Wife @I2@ is 25 or more year older than husband @I1@.',
                    'Wife @I12@ is 25 or more year older than husband @I13@.',
                    'Husband @I38@ is 25 or more year older than wife @I39@.',
                    'Husband @I1@ is 25 or more year older than wife @I25@.',
                    'Husband @I42@ is 25 or more year older than wife @I41@.',
                    'Husband @I49@ is 25 or more year older than wife @I48@.',
                    'Wife @I46@ is 25 or more year older than husband @I47@.',
                    'Wife @I41@ is 25 or more year older than husband @I44@.']

        # generating a list of the output from the function
        result = [value for value in US_47(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case

    def test_US_48(self):
        """ The function is to test US_48 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ['Wife @I2@ is older than husband @I1@.',
                    'Wife @I2@ is older than husband @I27@.',
                    'Wife @I2@ is older than husband @I26@.',
                    'Wife @I4@ is older than husband @I1@.',
                    'Wife @I46@ is older than husband @I47@.',
                    'Wife @I41@ is older than husband @I44@.']

        # generating a list of the output from the function
        result = [value for value in US_48(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(result == ['Birthdate "2022-01-01" for individual id @I1@ is illeagal',
                                    'Birthdate "2020-12-06" for individual id @I13@ is illeagal'])  # Negative test case


if __name__ == "__main__":
    """ Runs all the tests created above. """
    unittest.main(exit=False, verbosity=2)
