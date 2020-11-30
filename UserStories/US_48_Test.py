import unittest
from UserStories.US_48 import US_48
from Programs.Repository import Repository


class Test(unittest.TestCase):
    """For testing user story us01"""

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
    unittest.main(exit=False)
