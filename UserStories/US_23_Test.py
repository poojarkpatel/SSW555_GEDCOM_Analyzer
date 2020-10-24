import unittest
from Base_File import Repository
import datetime
from US_23 import US_23


class US_23_Test(unittest.TestCase):
    def test_one(self):
        expected = {'Mike /Robinson/': datetime.date(2021, 7, 2)}
        indi_repo: Repository = Repository("ssw555_input_file.ged")
        actual = US_23(indi_repo.individual)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)