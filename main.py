import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def process_text(file):
    print(file)
    ##dataframe = pd.read_csv(file)
    

def join_directory(path1, path2):
    
    joined_path = os.path.join(path1, path2)
    return joined_path


def find_file(file):
    
    user_directory = os.path.expanduser("~")
    downloads_folder = join_directory(user_directory, "Downloads")
    file_path = join_directory(downloads_folder, file)
    
    if os.path.exists(file_path):
        return file_path
    else:
        raise FileNotFoundError(f"File '{file}' was not found in '{downloads_folder}' folder..")

def main():
    try:
        file = find_file("spam.csv")
        print(f"File was found: {file}")
        process_text(file)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()