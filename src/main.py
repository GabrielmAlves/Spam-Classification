from data_processing import (
    process_text,
)
from data_split import (
    sets_division
)
from utils import (
    find_file,
)


def main():
    try:
        file = find_file("spam.csv")
        print(f"File was found: {file}")
        processed_file = process_text(file)
        X_train, X_val, X_test, y_train, y_val, y_test = sets_division(processed_file)
        
        print(f"\nX_train: {X_train}")
        print(f"\n\nX_val: {X_val}")
        print(f"\n\nX_test: {X_test}")
        print(f"\n\ny_train: {y_train}")
        print(f"\n\ny_val: {y_val}")
        print(f"\n\ny_test: {y_test}")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()