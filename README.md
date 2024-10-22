This project is a part of Masters program assignment on Deep Neural Networks

# Sentiment Analysis using LSTM on IMDB Dataset

This project implements a sentiment analysis model using a Long Short-Term Memory (LSTM) neural network. The model is trained on the IMDB movie reviews dataset to classify the sentiment of movie reviews as either positive or negative.

### Model Architecture

The model is built using the following architecture:

    Embedding Layer: Converts words into dense vectors of fixed size.
    LSTM Layer 1: First LSTM layer with 64 units, returns sequences to pass to the next LSTM layer.
    LSTM Layer 2: Second LSTM layer with 32 units, outputs a single sequence for the Dense layers.
    Dense Layer 1: Fully connected layer with 16 units and ReLU activation.
    Dense Layer 2: Fully connected layer with 1 unit and sigmoid activation for binary classification.

### Results

    Training Accuracy: 99%
    Test Accuracy: 81%
    The model provides strong generalization and performs well on new, unseen sentences.

### Dataset

The model is trained on the IMDB movie reviews dataset, which contains 25,000 labeled movie reviews (positive or negative). The dataset is preprocessed by converting the reviews into sequences of word indices.

### Conclusion

This LSTM-based model provides good sentiment analysis performance, making it suitable for understanding sentiment from text data in real-world application