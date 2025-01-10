import os
import chardet
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

def vectorize(messages):
    vectorizer = CountVectorizer(stop_words='english')
    
    X = vectorizer.fit_transform(messages)

    print("Vocabulary:", vectorizer.vocabulary_)
    print("\nCount matrix:")  
    print(X.toarray())

def encode(labels):
    label_encoder = LabelEncoder()
    
    encoded_values = label_encoder.fit_transform(labels)
    print(f"Original values: '{labels}'")
    print(f"Encoded values: '{encoded_values}'")
    return encoded_values

def process_text(file):
    with open(file, 'rb') as f:
        detection = chardet.detect(f.read())
        encoding = detection['encoding']
    
    dataframe = pd.read_csv(file, encoding=encoding)
    print(dataframe.head())
    
    labels = dataframe['v1']
    messages = dataframe['v2']
    
    encoded_labels = encode(labels)
    encoded_messages = vectorize(messages)    

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