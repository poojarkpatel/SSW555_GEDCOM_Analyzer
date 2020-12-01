import unittest
from UserStories.US_21 import US_21
from Programs.Base_File import Repository

class US_21_test(unittest.TestCase):
    def test_US_21(self):
        """ Function that tests user story 21 """
        repository = Repository("../GedcomFiles/SSW_555_updatedwithUS_2_3.ged")
        expected = ['US_21: Sam /Robinson/ gender is supposed to be female but is not on line number 269']
        actual = US_21(repository.get_individual(), repository.get_family())
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
