from guizero import App, TextBox, PushButton, Text
import pickle
import numpy as np


with open("ML/models/spam_classifier.pkl", "rb") as model_file:
    classifier = pickle.load(model_file)

with open("ML/models/tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    tfvec = pickle.load(vectorizer_file)

print("Model và vectorizer đã được load thành công!")

# def check_spam():
#     email_text = email_input.value
#     email_vector = tfvec.transform([email_text]).toarray()
#     prediction = classifier.predict(email_vector)[0]
#     result.value = "Spam!" if prediction == 1 else "Ham (Not Spam)"

def check_spam():
    email_text = email_input.value.strip()
    email_vector = tfvec.transform([email_text])
    prediction = classifier.predict(email_vector)[0]
    result.value = "Spam!" if prediction == 1 else "Ham (Not Spam)"

# GUI
app = App(title="Email Spam Classifier", width=400, height=250)

Text(app, text="Nhập nội dung email:")
email_input = TextBox(app, width=50, height=5, multiline=True)
check_button = PushButton(app, text="Kiểm tra", command=check_spam)
result = Text(app, text="")

app.display()
