import pandas as pd
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.event_detection import detect_event_description
from src.utils import evaluate_model

def main():
    data = pd.read_csv('data/historical_event_data.csv')
    
    X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer = preprocess_data(data)
    model = train_model(X_train_tfidf, y_train)
    
    evaluation_report = evaluate_model(model, X_test_tfidf, y_test)
    print("Classification Report:\n", evaluation_report)
    
    incoming_event = "User JohnDoe attempted to access restricted files."
    prediction = detect_event_description(model, vectorizer, incoming_event)
    
    if prediction == 1:
        print("Suspicious: Potential privilege escalation detected.")
    else:
        print("Normal event.")

if __name__ == "__main__":
    main()
