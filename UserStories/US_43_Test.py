"""
Author: Priyankaben Shyiani
SSW 555 Agile Methods for Software Development
Purpose: Testing for user story 43
"""
import unittest
from UserStories.US_43 import US_43
from Programs.Base_File import Repository

class Test(unittest.TestCase):
    def test_US_43(self):
        """ Contains test cases for US_43"""
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = ['Emmy /Robinson/ is divorced and alive on line number 151',
                    'Tia /Ale/ is divorced and alive on line number 324',
                    'Micheal /Mia/ is divorced and alive on line number 343',
                    'Mike /Robinson/ is divorced and alive on line number 333']
        actual = US_43(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)