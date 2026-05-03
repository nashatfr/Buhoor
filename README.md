<h1 align="center">🌙 Buhoor — Arabic Poetry Meter Classifier (بحور الشعر)</h1>

<p align="center">
  <em>An intelligent deep learning system that understands the rhythm of Arabic poetry.</em>
</p>

---

## 🎥 Demo

<!-- Note: GitHub will automatically render this link as an embedded video player. -->
https://github.com/nashatfr/Buhoor/raw/main/demo.mp4

---

## ✨ What is Buhoor?

**Buhoor** is a deep learning system that analyzes an Arabic verse and predicts its **poetic meter (بحور الشعر)**.

In simple terms:

> You enter a line of Arabic poetry (بيت شعري), and Buhoor identifies its classical rhythm — just like an expert in Arabic prosody (العَروض).

**It is designed to make Arabic poetry analysis:**
- 📖 **Easier** for students
- ⚡ **Faster** for researchers
- 🌍 **Accessible** for anyone interested in classical Arabic literature

---

## 🧠 How it works

The system reads the input verse as a sequence of characters and learns hidden patterns in Arabic poetic structure using a deep neural network. 

It then predicts the most likely meter from the classical Arabic **بحور الشعر**.

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

