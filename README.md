> A deep learning model that understands the rhythm of Arabic poetry.

---

## 🎥 Demo

https://github.com/nashatfr/Buhoor/blob/main/demo.mp4

---

## ✨ What is Buhoor?

**Buhoor** is a deep learning model that analyzes an Arabic verse and predicts its **poetic meter (بحور الشعر)**.

In simple terms:

> You enter a verse of Arabic poetry (بيت شعري), and Buhoor instantly identifies its classical meter — like an expert in Arabic prosody (العَروض).

Normally, determining the correct meter requires multiple manual steps:

- Writing the verse  
- Phonetic pronunciation (التقطيع الصوتي)  
- Identifying syllable patterns  
- Matching against classical meters  

**Buhoor replaces all of these steps with a single prediction.**

It is designed to make Arabic poetry analysis:
- Easier for students  
- Faster for researchers  
- More accessible for anyone studying classical Arabic literature

## 🏗️ Model Overview

The model is built using a **deep learning architecture based on Embedding layers and Bidirectional LSTMs**.

- An **Embedding layer** converts characters into dense vector representations  
- **Bidirectional LSTM layers** capture poetic structure from both directions  
- **Layer Normalization + Dropout** improve stability and prevent overfitting  
- A **Dense softmax layer** outputs probabilities across all poetic meters  

---

## 📊 Dataset

Trained on the **Ashaar Dataset (أشعار)** — a collection of classical Arabic poetry used for learning and evaluating Arabic poetic meters.

---

## 📈 Model Performance

The model was evaluated on a held-out test set in the training notebook:

- **Test Accuracy: 94.96%**

This shows that the model is able to reliably classify Arabic poetic meters with high accuracy across different verse patterns.

---

## 🚀 Try it yourself

You can test the model directly using the Streamlit app:

> Enter your favorite Arabic verses (بيوت شعرية) and see the predicted meter instantly.

```bash
streamlit run app.py
