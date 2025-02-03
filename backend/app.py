from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Correct the variable name to "vectorizer"
model = joblib.load("models/fake_news_detect.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer.joblib")


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    
    # Transform text using the vectorizer
    text_vectorized = vectorizer.transform([text])  # Use the correct vectorizer variable
    
    # Predict using the model
    prediction = model.predict(text_vectorized)[0]
    
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)



