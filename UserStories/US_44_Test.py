"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: Testing for user story 44
"""
import unittest
from UserStories.US_44 import US_44
from Programs.Base_File import Repository

class Test(unittest.TestCase):
    def test_US_44(self):
        """ Contains test cases for US_44"""
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = ['Priyanka /Robinson/ is alive and age is more than 100 years old on line '
                    'number 34',
                    'Emmy /Robinson/ is alive and age is more than 100 years old on line number '
                    '151',
                    'Yatinkumar /Shiyani/ is alive and age is more than 100 years old on line '
                    'number 292',
                    'Ginger /Ale/ is alive and age is more than 100 years old on line number 312',
                    'Tia /Ale/ is alive and age is more than 100 years old on line number 324']
        actual = US_44(repository.get_individual())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)