from data_processing import (
    process_text,
)
from data_split import (
    sets_division
)
from utils import (
    find_file,
)
from modeling import (
    train_model,
    evaluate_model,
)


def main():
    try:
        file = find_file("spam.csv")
        print(f"File was found: {file}")
        processed_file = process_text(file)
        X_train, X_val, X_test, y_train, y_val, y_test = sets_division(processed_file)
        model, vectorizer = train_model(X_train, y_train, X_val, y_val)
        evaluate_model(model, vectorizer, X_test, y_test)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()