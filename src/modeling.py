from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer

def train_model(X_train, y_train, X_val, y_val):
    random_forest_model = RandomForestClassifier(criterion='entropy', max_depth=100, n_estimators=100, random_state=42)
    
    
    vectorizer = CountVectorizer(stop_words='english')
    X_train_vect = vectorizer.fit_transform(X_train)
    X_val_vect = vectorizer.transform(X_val)
    
    random_forest_model.fit(X_train_vect, y_train)
    print(f"Model trained successfully!")
    
    y_val_pred = random_forest_model.predict(X_val_vect)
    accuracy = accuracy_score(y_val, y_val_pred)
    
    print(f"Validation Accuracy: {accuracy:.2f}")

    print("Classification Report:")
    print(classification_report(y_val, y_val_pred))

    return random_forest_model, vectorizer
    