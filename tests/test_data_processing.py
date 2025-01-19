import os
import pandas as pd
import unittest
from src.data_processing import (
    process_text,
    encode,
    vectorize,
)
from src.utils import (
    find_file,
)

class UnitTestDataProcessing(unittest.TestCase):
    
    def test_find_file_exists(self):
        test_file = "spam.csv"
        with open(test_file, 'w') as f:
            f.write("v1,v2\nham,Hello\nspam,Buy now!")
            
        self.assertEqual(find_file(test_file, folder="."), os.path.abspath(test_file))
        os.remove(test_file)    

if __name__ == "__main__":
    unittest.main()