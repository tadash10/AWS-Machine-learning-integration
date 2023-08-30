def detect_event_description(model, vectorizer, incoming_event):
    incoming_event_tfidf = vectorizer.transform([incoming_event])
    prediction = model.predict(incoming_event_tfidf)
    return prediction[0]
