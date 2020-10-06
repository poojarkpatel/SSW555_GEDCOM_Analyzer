import unittest
from Base_File import Repository
from US_17 import US_17

class US_17_Test(unittest.TestCase):
    def test_one(self):
        expected = {'Joey /Robinson/': 'Monica /Geller/'}
        indi_repo: Repository = Repository("ssw555_input_file.ged")
        actual = US_17(indi_repo._family.values())
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)