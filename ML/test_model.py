import pickle

with open("ML/models/spam_classifier.pkl", "rb") as model_file:
    classifier = pickle.load(model_file)

with open("ML/models/tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    tfvec = pickle.load(vectorizer_file)

print("Classifier type:", type(classifier))
print("Vectorizer type:", type(tfvec))
