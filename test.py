import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load historical event data (Assuming CSV format with 'event_description' and 'is_privilege_escalation' columns)
data = pd.read_csv('historical_event_data.csv')

# Data preprocessing
X = data['event_description']
y = data['is_privilege_escalation']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Now let's assume you have an incoming event description
incoming_event = "User JohnDoe attempted to access restricted files."

# Preprocess the incoming event description
incoming_event_tfidf = vectorizer.transform([incoming_event])

# Use the trained model to predict if it's a privilege escalation event
prediction = model.predict(incoming_event_tfidf)

if prediction[0] == 1:
    print("Suspicious: Potential privilege escalation detected.")
else:
    print("Normal event.")
