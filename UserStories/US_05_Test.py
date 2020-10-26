"""
Test cases for user story US_05
Author: Varun Mullins
"""

import unittest
from UserStories.US_05 import US_05
from Programs.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_05"""

    def test_us05(self):
        """ The function is to test US_05 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ["Marriage date Line: 501\nDeath of wife date Line: 60\n"
                    "The family @F14@ has a death of wife @I4@ before the marriage date."]

        # generating a list of the output from the function
        result = [value for value in US_05(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case


if __name__ == "__main__":
    unittest.main(exit=False)