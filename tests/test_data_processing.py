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
    join_directory
)

class UnitTestDataProcessing(unittest.TestCase):
    
    def test_find_file_exists(self):
        test_file = "spam.csv"
        downloads_path = join_directory(os.path.expanduser("~"), "Downloads")
        file_path = join_directory(downloads_path, test_file)
        print(file_path)
        self.assertTrue(os.path.exists(file_path), f"File {test_file} is not on Downloads folder..")
        # with open(test_file, 'w') as f:
        #     f.write("v1,v2\nham,Hello\nspam,Buy now!")
            
        # self.assertEqual(find_file(test_file), os.path.abspath(test_file))
        # os.remove(test_file)    

if __name__ == "__main__":
    unittest.main()