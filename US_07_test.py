import unittest
from US_07 import US_07
from Base_File import Repository


class Test(unittest.TestCase):

    def test_US_07(self):
        """ Contains test cases for US_07"""
        indi_repo: Repository = Repository("US_07.ged")

        expected = ["Tia /Ale/"]

        self.assertEqual(US_07(indi_repo.individual), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)