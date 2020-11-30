import unittest
from UserStories.US_52 import US_52
from Programs.Base_File import Repository


class Test(unittest.TestCase):

    def test_US_52(self):
        """ Contains test cases for US_52"""
        indi_repo = Repository("../GedcomFiles/US_52.ged")

        expected = [
            'US 50: Joey /Robinson/', 'US 50: Ross /Robinson/', 'US 50: Ben /Mann/', 'US 50: Mike /Robinson/', 'US 50: William /Robinson/',
            'US 50: Max /Robinson/', 'US 50: Jimmy /Smith/', 'US 50: Miller /Robinson/', 'US 50: Sam /Robinson/', 'US 50: Ross /Robinson/',
            'US 50: Sam /Robinson/', 'US 50: Joss /Parker/', 'US 50: Yatinkumar /Shiyani/', 'US 50: Ginger /Ale/', 'US 50: Mike /Robinson/',
            'US 50: Ryan /Robinson/', 'US 50: Mike /Robinson/', 'US 50: Ribu /Watson/']

        self.assertEqual(US_52(indi_repo._individual), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)