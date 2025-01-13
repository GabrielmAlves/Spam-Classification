from utils import (
    get_column
)

def sets_division(dataframe):
    labels = get_column(dataframe, 'v1')
    features = get_column(dataframe, 'v2')
    print(f"features: \n", features)