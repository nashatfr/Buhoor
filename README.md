<h1 align="center">🌙 Buhoor — Arabic Poetry Meter Classifier (بحور الشعر)</h1>
<p align="center"><em>An intelligent deep learning system that understands the rhythm of Arabic poetry.</em></p>
---


## 🎥 Demo
<p align="center">
  <video src="https://github.com/nashatfr/Buhoor/raw/main/assets/demo.mp4" width="100%" height="auto" autoplay muted loop></video>
</p>
<!-- If autoplay is restricted by GitHub, the video will still appear as a playable embed below -->
https://github.com/nashatfr/Buhoor/raw/main/assets/demo.mp4


---
## ✨ Why Buhoor?
Traditionally, identifying a poetic meter is a grueling manual process requiring four distinct stages of **Ilm al-Arud (علم العروض)**:
* **1. الكتابة العروضية (Arud Writing):** Rewriting the verse phonetically (e.g., writing *Shaddah* as two letters).
* **2. الترميز (Symbolization):** Manually mapping every single letter to a moving (/) or silent (o) stroke.
* **3. التفاعيل (Poetic Feet):** Deciphering how those symbols group into rhythmic units like *Fa'ulun* or *Mustaf'ilun*.
* **4. المطابقة (Matching):** Checking the resulting pattern against the 16 classical Arabic meters.
**Buhoor eliminates this entire workflow.** You simply enter the raw verse, and the deep learning model skips the manual encoding, instantly identifying the rhythm through its trained "musical ear."
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
