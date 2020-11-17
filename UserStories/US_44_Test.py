import unittest
from UserStories.US_44 import US_44
from Programs.Base_File import Repository

class Test(unittest.TestCase):
    def test_US_44(self):
        """ Contains test cases for US_44"""
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = ['Priyanka /Robinson/',
                    'Emmy /Robinson/',
                    'Yatinkumar /Shiyani/',
                    'Ginger /Ale/',
                    'Tia /Ale/']
        actual = US_44(repository.get_individual())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)