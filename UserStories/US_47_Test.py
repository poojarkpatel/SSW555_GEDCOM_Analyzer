import unittest
from UserStories.US_47 import US_47
from Programs.Repository import Repository


class Test(unittest.TestCase):
    """For testing user story us01"""

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


if __name__ == "__main__":
    unittest.main(exit=False)
