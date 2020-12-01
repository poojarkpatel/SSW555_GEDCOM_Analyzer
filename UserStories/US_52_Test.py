import unittest
from UserStories.US_52 import US_52
from Programs.Base_File import Repository


class Test(unittest.TestCase):

    def test_US_52(self):
        """ Contains test cases for US_52"""
        indi_repo = Repository("../GedcomFiles/US_52.ged")

        expected = {'Ryan /Robinson/', 'Jimmy /Smith/', 'Ginger /Ale/', 'William /Robinson/', 'Sam /Robinson/', 'Miller /Robinson/', 'Joey /Robinson/', 'Max /Robinson/', 'Ross /Robinson/', 'Joss /Parker/', 'Yatinkumar /Shiyani/', 'Ribu /Watson/', 'Mike /Robinson/', 'Ben /Mann/'}

        self.assertEqual(US_52(indi_repo._individual), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)