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
        sets_division(processed_file)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()