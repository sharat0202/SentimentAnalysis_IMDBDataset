from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Max length for input sequences
max_length = 200

# Load the pre-trained LSTM model
model = load_model('lstm_model.h5')
word_index = imdb.get_word_index()


def preprocess_text(text):
    """Preprocess text to match the format used during training"""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Convert words to integers using the word_index
    sequence = []
    for word in words:
        if word in word_index:
            sequence.append(word_index[word] + 3)  # Add 3 for special tokens
        else:
            sequence.append(2)  # Unknown word token
    
    # Pad sequence
    padded_sequence = pad_sequences([sequence], maxlen=max_length)
    
    return padded_sequence

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    # Get data from request
    data = request.get_json()
    
    text = data['text']
        
    # Preprocess the text
    processed_text = preprocess_text(text)
        
    # Make prediction
    prediction = model.predict(processed_text)[0][0]
    
    # Prepare response
    sentiment = 'Positive' if prediction > 0.5 else 'Negative'
    
    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'raw_score': float(prediction)
    })

# Define a route for testing
@app.route('/')
def index():
    return "Sentiment Analysis API is running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
