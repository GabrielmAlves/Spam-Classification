from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from data_processing import (
    vectorize,
)
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, vectorizer, X_test, y_test):
    
    X_test_vect = vectorize(X_test, vectorizer, fit=False)
    
    y_test_pred = model.predict(X_test_vect)
    accuracy = accuracy_score(y_test, y_test_pred)
    print(f"Test Accuracy: {accuracy:.2f}")

    print("Classification Report:")
    print(classification_report(y_test, y_test_pred))
    
    confusion_matrix_report = confusion_matrix(y_test, y_test_pred)
    print(f"\nConfusion Matrix: \n")
    print(confusion_matrix_report)


def train_model(X_train, y_train, X_val, y_val):
    random_forest_model = RandomForestClassifier(criterion='entropy', max_depth=100, n_estimators=100, random_state=42)
    vectorizer = CountVectorizer(stop_words='english')
    
    X_train_vect = vectorize(X_train, vectorizer, fit=True)
    X_val_vect = vectorize(X_val, vectorizer, fit=False)
    
    random_forest_model.fit(X_train_vect, y_train)
    print(f"Model trained successfully!")
    
    y_val_pred = random_forest_model.predict(X_val_vect)
    accuracy = accuracy_score(y_val, y_val_pred)
    
    print(f"Validation Accuracy: {accuracy:.2f}")
    print(f"Classification Report: \n" + classification_report(y_val, y_val_pred))
    
    return random_forest_model, vectorizer