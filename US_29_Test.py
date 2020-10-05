import unittest
from Base_File import Repository,US_29
from typing import List
import datetime

class TestRepository(unittest.TestCase):
 
    def test_deceased(self):
            indi_repo: Repository = Repository("US_29.ged")
            excepted: List=[['Joey /Robinson/', 'Ross /Robinson/', 'Monica /Geller/',
            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/', 'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']]
            expected1:List=[['Joey /Robinson/', 'Ross /Robinson/',
            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/', 'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']]
            excepted2: List=[['Joey /Robinson/', 'Ross /Robinson/', 'Monica /Geller/',
            'Ben /Mann/', 'Mike /Robinson/', 'Rachel /Green/', 'Ema /Mosbi/', 'William /Robinson/', 'Max /Robinson/', 'Dora /Robinson/', 'Jimmy /Smith/']
            ,['Htp /Manan/']]
        
            #calculated = [individual.info_individual() for individual in indi_repo._individual.values()]
            calculated=[[i for i in US_29(indi_repo)]]
            self.assertEqual(sorted(calculated),sorted(excepted))
            self.assertNotEqual(calculated,expected1)
            self.assertGreaterEqual(len(calculated),len(expected1))
            self.assertLess(len(calculated),len(excepted2))
            self.assertNotEqual(calculated,excepted2)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)            
