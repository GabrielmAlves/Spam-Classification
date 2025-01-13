import os
import chardet
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from utils import (
    get_column
)

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
    
    labels = get_column(dataframe, 'v1')
    encoded_labels = encode(labels)
    
    dataframe['v1'] = encoded_labels
    return dataframe