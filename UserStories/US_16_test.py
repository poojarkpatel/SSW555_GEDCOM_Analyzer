import unittest
from UserStories.US_16 import US_16
from Programs.Base_File import Repository

class Test(unittest.TestCase):

    def test_US_16(self):
        """ Contains test cases for US_16"""
        indi_repo: Repository = Repository("../GedcomFiles/US_16.ged")

        expected = ['US_16: Family id @F15@ with father Ribu /Watson/ and son Joey /Robinson/ have different last names on line number 503',
                    'US_16: Family id @F15@ with father Ribu /Watson/ and son Sam /Robinson/ have different last names on line number 503',
                    'US_16: Family id @F2@ with father Ross /Robinson/ and son Ben /Mann/ have different last names on line number 407',
                    'US_16: Family id @F2@ with father Ross /Robinson/ and son Ginger /Ale/ have different last names on line number 407' ]

        self.assertEqual(US_16(indi_repo._individual ,indi_repo._family), expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)