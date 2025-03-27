from guizero import App, TextBox, PushButton, Text, Box
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
    
    # Kiểm tra nếu ô nhập trống
    if not email_text:
        result.value = "⚠️ Vui lòng nhập nội dung email!"
        result.text_color = "red"
        return
 
    email_vector = tfvec.transform([email_text])
    prediction = classifier.predict(email_vector)[0]
    if prediction == 1:
        result.value = "❌ Spam!"
        result.text_color = "red"
    else:
        result.value = "✅ Ham (Not Spam)"
        result.text_color = "green"

# # GUI
# app = App(title="Email Spam Classifier", width=400, height=250)

# Text(app, text="Nhập nội dung email:")
# email_input = TextBox(app, width=50, height=5, multiline=True)
# check_button = PushButton(app, text="Kiểm tra", command=check_spam)
# result = Text(app, text="")

# app.display()

app = App(title="Kiểm tra Email Spam", width=650, height=300, layout="auto", bg="#f0f0f0")

title = Text(app, text="\U0001F4E7 Kiểm tra thư rác", size=16, font="Arial", color="#333333")
Text(app, text="", size=10)

Text(app, text="", size=10)
input_box = Box(app, layout="grid")
Text(input_box, text="\U0001F4E9 Nhập email:", grid=[0,0], align="left")
Text(app, text="", size=10)
email_input = TextBox(input_box, width=40, height=5, multiline=True, grid=[1,0], scrollbar=True)

Text(app, text="", size=10)
check_button = PushButton(app, text="Kiểm tra ngay", command=check_spam)
check_button.text_size = 12
check_button.bg = "#007bff"
check_button.text_color = "white"

result = Text(app, text="", size=14, font="Arial", color="black")

app.display()
