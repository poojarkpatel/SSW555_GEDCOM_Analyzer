"""
Test cases for user story US_09
Author: Varun Mullins
"""

import unittest
from UserStories.US_09 import US_09
from Programs.Base_File import Repository


class Test(unittest.TestCase):
    """For testing user story US_05"""

    def test_us09(self):
        """ The function is to test US_09 function"""
        indi_repo: Repository = Repository('../GedcomFiles/ssw555_input_file.ged')

        # The expected output
        expected = ["Family id Line number: 398\n"
                    "Birth of child @I28@ is before the death of the father @I27@",
                    "Family id Line number: 398\n"
                    "Birth of child @I28@ is before the death of the mother @I2@",
                    "Family id Line number: 407\n"
                    "Birth of child @I35@ is before the death of the father @I3@",
                    "Family id Line number: 407\n"
                    "Birth of child @I35@ is before the death of the mother @I4@",
                    "Family id Line number: 407\n"
                    "Birth of child @I31@ is before the death of the father @I3@",
                    "Family id Line number: 407\n"
                    "Birth of child @I31@ is before the death of the mother @I4@"]

        # generating a list of the output from the function
        result = [value for value in US_09(indi_repo._individual, indi_repo._family)]

        self.assertEqual(result, expected)  # positive test result
        self.assertFalse(
            result == ['The family @F11@ has a death of wife @I7@ before the marriage date.'])  # Negative # test case


if __name__ == "__main__":
    unittest.main(exit=False)
