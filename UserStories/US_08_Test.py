"""
Test cases for user story US_08
Author: Varun Mullins
"""

import unittest
from UserStories.US_08 import US_08
from Programs.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_08"""

    def test_US_08(self):
        """ The function is to test US_08 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ["Family id Line number: 391\nThe Father @I1@ is younger than his child @I4@ which is "
                    "illeagal.",
                    "Family id Line number: 484\nThe Father @I31@ is younger than his child @I33@ which is "
                    "illeagal.",
                    "Family id Line number: 503\nThe Father @I36@ is younger than his child @I1@ which is "
                    "illeagal."]

        # generating a list of the output from the function
        result = [value for value in US_08(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case