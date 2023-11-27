import json
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

# Load the JSON file
file_path = 'Groups/Overall_data/BasisURLs.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract URLs from the data
urls = [entry['URL'] for entry in data]

# Concatenate all URLs to create a corpus
corpus = ''.join(urls)

# Create a character mapping
chars = sorted(list(set(corpus)))
char_to_index = {char: index for index, char in enumerate(chars)}
index_to_char = {index: char for index, char in enumerate(chars)}

# Generate training data
seq_length = 50
sequences = []
next_chars = []
for i in range(len(corpus) - seq_length):
    seq = corpus[i:i + seq_length]
    next_char = corpus[i + seq_length]
    sequences.append([char_to_index[char] for char in seq])
    next_chars.append(char_to_index[next_char])

# Convert to numpy arrays
X = np.array(sequences)
y = np.array(next_chars)

# One-hot encode the labels
y_one_hot = to_categorical(y, num_classes=len(chars))

# Reshape X to be (samples, time steps, features)
X = np.reshape(X, (X.shape[0], seq_length, 1))

# Normalize the input data
X = X / float(len(chars))

# Build the model
model = Sequential()
model.add(LSTM(128, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(len(chars), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(X, y_one_hot, epochs=10, batch_size=128)

# Function to generate new URLs
def generate_url(model, seed, length=50):
    generated = seed
    for _ in range(length):
        x = np.reshape([char_to_index[char] for char in seed[-seq_length:]], (1, seq_length, 1)) / float(len(chars))
        prediction = model.predict(x, verbose=0)
        index = np.argmax(prediction)
        result = index_to_char[index]
        generated += result
        seed = seed[1:] + result
    return generated

# Generate new URLs based on the existing ones
for url in urls:
    generated_url = generate_url(model, seed=url, length=50)
    print(generated_url)
