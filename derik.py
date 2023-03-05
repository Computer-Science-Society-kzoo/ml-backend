import tensorflow as tf
from tensorflow import keras
import numpy as np
import nltk
import sys

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
# Create blank dictionary to store words and vectors
words = dict()

# Function to add words and vectors to dictionary
def add_to_dict(d, filename):
  # Open the file
  with open(filename, 'r') as f:
    # Iterate through the file and each line
    for line in f.readlines():
      # Split the line into words based on space
      line = line.split(' ')

      try:
        # Add the word and vector to the dictionary
        # We are going to try to keep the vector to the corresponding data type
        d[line[0]] = np.array(line[1:], dtype=float)
      except:
        continue

add_to_dict(words, 'models/d/glove.6B.50d.txt')

# We need to tokenize and so we create a tokenizer
tokenizer = nltk.RegexpTokenizer(r"\w+")

# We need to lemmatize the words
# Lemmatization converts words to their more common root form
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Example feet -> foot
lemmatizer.lemmatize('feet')

# Give the function a string and convert to token then to lemmatized token as list
def message_to_token_list(s):
  # Tokenize the string
  tokens = tokenizer.tokenize(s)
  # Convert to lower case
  lowercased_tokens = [t.lower() for t in tokens]
  # Lemmatize the tokens
  lemmatized_tokens = [lemmatizer.lemmatize(t) for t in lowercased_tokens]
  # Remove tokens that are not in the dictionary
  useful_tokens = [t for t in lemmatized_tokens if t in words]

  return useful_tokens

# Grab the list of words and turn them into a vector
def message_to_word_vectors(message, word_dict=words):
  processed_list_of_tokens = message_to_token_list(message)

  vectors = []

  for token in processed_list_of_tokens:
    if token not in word_dict:
      continue
    
    token_vector = word_dict[token]
    vectors.append(token_vector)
  
  return np.array(vectors, dtype=float)


from copy import deepcopy

def pad_X(X, desired_sequence_length=57):
  X_copy = deepcopy(X)

  for i, x in enumerate(X):
    x_seq_len = x.shape[0]
    sequence_length_difference = desired_sequence_length - x_seq_len
    
    pad = np.zeros(shape=(sequence_length_difference, 50))

    X_copy[i] = np.concatenate([x, pad])
  
  return np.array(X_copy).astype(float)



def make_prediction(model, X_new):

    X_new = message_to_word_vectors(X_new)

    X_new = pad_X([X_new])

    predict_x = model.predict(X_new) 
    classes_x = np.argmax(predict_x, axis=1)
    return classes_x

reconstructed_model = keras.models.load_model("models/d/neural_model")


input_1 = sys.argv[1]
prediction = make_prediction(reconstructed_model, input_1)

if prediction == 0:
    print("Not Confident")
elif prediction == 1:
    print("Neutral")
else:
    print("Confident")