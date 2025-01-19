import os
import chardet
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from src.utils import (
    get_column
)

def vectorize(set, vectorizer, fit=False):
    if fit:
        return vectorizer.fit_transform(set)
    else:
        return vectorizer.transform(set)

def encode(labels):
    label_encoder = LabelEncoder()
    
    encoded_values = label_encoder.fit_transform(labels)
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