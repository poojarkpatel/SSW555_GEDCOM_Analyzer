"""
Author:Priyankaben Shiyani
SSW 555 Agile Methods for Software Development 
Purpose: Testing for user story 11
"""
import unittest, os, io, sys
from Base_File import Repository , Individual, Family
from US_11 import US_11


class Test_US11(unittest.TestCase):
    """ Tests that husbands and wifes are not married twice at the same time. """

    def test_US_11(self):
        """ Tests that husbands and wifes are not married twice at the same time and prints out the cases if so"""
        indi_repo = Repository('US_11.ged')
        output = ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time']
        self.assertEqual(US_11(indi_repo), output)
        self.assertNotEqual(US_11(indi_repo), ['Ross /Galler married twice on the same time'])
        self.assertTrue(US_11(indi_repo) == ['Joey /BIng/married twice at the same time', 'Rachel /Green/married twice at the same time'])
        self.assertFalse(US_11(indi_repo) == ['Emma /Galler married twice on the same time'])
        self.assertTrue(US_11(indi_repo) != ['Ross /Galler married twice on the same time'])


if __name__ == "__main__":
    unittest.main(exit=False)

