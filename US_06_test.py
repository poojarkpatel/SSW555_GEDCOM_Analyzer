import unittest
from US_06 import US_06
from Base_File import Repository


class Test(unittest.TestCase):

    def test_US_06(self):
        """ Contains test cases for US_06"""
        indi_repo: Repository = Repository("US_06.ged")

        expected = ["US_06: Katir /Bala/ Death 1822-01-03 occured prior to the divorce date 1852-07-14"]

        self.assertEqual((US_06(indi_repo._individual, indi_repo._family)), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)