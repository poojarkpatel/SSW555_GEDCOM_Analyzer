"""
Test cases for user story US_05
Author: Varun Mullins
"""

import unittest
from UserStories.US_10 import US_14
from Programs.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_14"""

    def test_us14(self):
        """ The function is to test US_14 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ["Family id Line number: 484\n"
                    "The husband @I31@ was younger than 14 at the time of marriage for @F13@",
                    "Family id Line number: 484\n"
                    "The wife @I32@ was younger than 14 at the time of marriage for @F13@",
                    "Family id Line number: 510\n"
                    "The wife @I25@ was younger than 14 at the time of marriage for @F20@"]

        # generating a list of the output from the function
        result = [value for value in US_14(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case


if __name__ == "__main__":
    unittest.main(exit=False)
