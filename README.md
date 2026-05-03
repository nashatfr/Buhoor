<h1 align="center">🌙 Buhoor — Arabic Poetry Meter Classifier (بحور الشعر)</h1>
<p align="center"><em>An intelligent deep learning system that understands the rhythm of Arabic poetry.</em></p>
---
## 🎥 Demo
https://github.com/nashatfr/Buhoor/raw/main/assets/demo.mp4
---
## ✨ Why Buhoor?
Traditionally, identifying a poetic meter requires four tedious manual steps in **Ilm al-Arud (علم العروض)**:
* **1. الكتابة العروضية (Arud Writing):** Rewriting the verse exactly as pronounced (adding hidden letters, removing silent ones).
* **2. الترميز (Symbolization):** Mapping every letter to either a moving (/) or silent (o) state.
* **3. التفاعيل (Poetic Feet):** Grouping these symbols into prosodic units (e.g., *فعولن*, *مفاعيلن*).
* **4. المطابقة (Matching):** Comparing the sequence of feet against the 16 classical Arabic meters.

**Buhoor eliminates this process entirely.** Instead of performing these manual translations, you simply input the raw Arabic text. The deep learning model instantly predicts the correct meter by recognizing complex rhythmic patterns automatically, bypassing the need for manual symbolization or phonetic rewriting.
---
## 🧠 How it works
The system reads the input verse as a sequence of characters and learns hidden patterns in Arabic poetic structure using a deep neural network. It then predicts the most likely meter from the classical Arabic **بحور الشعر**.
---
## 🏗️ Model Overview
The model is built using a **deep learning architecture based on Embedding layers and Bidirectional LSTMs**.
* **Embedding layer:** Converts characters into dense vector representations.
* **Bidirectional LSTM layers:** Capture poetic structure from both directions.
* **Layer Normalization + Dropout:** Improve stability and prevent overfitting.
* **Dense softmax layer:** Outputs probabilities across all poetic meters.
---
## 📊 Dataset
Trained on the **Ashaar Dataset (أشعار)** — a collection of classical Arabic poetry used for learning and evaluating Arabic poetic meters.
---
## 📈 Model Performance
The model was evaluated on a held-out test set in the training notebook:
> 🏆 **Test Accuracy: 94.96%**

This shows that the model is able to reliably classify Arabic poetic meters with high accuracy across different verse patterns.
---
## 🚀 Try it yourself
You can test the model directly using the Streamlit app:
> Enter your favorite Arabic verses (بيوت شعرية) and see the predicted meter instantly.
```bash
streamlit run app.py
