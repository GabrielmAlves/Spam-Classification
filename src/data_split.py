from utils import (
    get_column
)
from sklearn.model_selection import train_test_split

def sets_division(dataframe):
    labels = get_column(dataframe, 'v1')
    features = get_column(dataframe, 'v2')
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=42)
    
    return X_train, X_val, X_test, y_train, y_val, y_test