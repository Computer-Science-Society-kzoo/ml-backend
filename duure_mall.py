import sys
import pickle

input_1 = sys.argv[1]

model = pickle.load(open("models/dm/tree_clf", "rb"))
vectorizer = pickle.load(open("models/dm/vectorizer", "rb"))
tfidf = pickle.load(open("models/dm/tfidf", "rb"))

inputCleaned = vectorizer.transform([input_1])

inputCleaned = tfidf.transform(inputCleaned)

prediction = model.predict(inputCleaned)

if prediction[0] == 0:
    print("neutral")
elif prediction[0] == 1:
    print("confident")
else:
    print("somehting went wrong: " + str(prediction[0]))
