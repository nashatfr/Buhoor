<div align="center">

<h1>بُحور &nbsp;·&nbsp; Buhoor</h1>

<p><strong>Arabic Poetry Meter Classifier — بحور الشعر</strong></p>

<p><em>An intelligent deep learning system that understands the rhythm of Arabic poetry.</em></p>

<br/>

![Python](https://img.shields.io/badge/Python-3.8+-c9933a?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-c9933a?style=flat-square&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-c9933a?style=flat-square&logo=streamlit&logoColor=white)
![Accuracy](https://img.shields.io/badge/Test%20Accuracy-94.96%25-2d6a2d?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-555?style=flat-square)

</div>

---

## ✨ Why Buhoor?

Traditionally, identifying a poetic meter is a grueling **four-stage** manual process called **Prosody (علم العروض)**:

| # | Stage | Arabic | Description |
|---|-------|--------|-------------|
| 1 | Arud Writing | الكتابة العروضية | Rewriting the verse phonetically — e.g., writing *Shaddah* as two letters |
| 2 | Symbolization | الترميز | Mapping every letter to a moving `/` or silent `o` stroke |
| 3 | Poetic Feet | التفاعيل | Grouping symbols into rhythmic units like *Fa'ulun* or *Mustaf'ilun* |
| 4 | Matching | المطابقة | Checking the pattern against the 16 classical Arabic meters |

> **Buhoor eliminates this entire workflow.**
> Enter the raw verse → get the meter. Instantly.

---

## 🧠 How It Works

The model reads the verse as a **sequence of characters** and learns hidden rhythmic patterns through a deep neural network — then predicts the most likely meter from the 16 classical Arabic meters.

No manual encoding. No prosody expertise required.

---

## 🎥 Demo

> Click the thumbnail below to watch the demo:

[![Watch Demo](https://img.shields.io/badge/▶%20Watch%20Demo-Click%20Here-c9933a?style=for-the-badge)](https://github.com/nashatfr/Buhoor/raw/main/assets/demo.mp4)

> 💡 **Tip:** To get autoplay in your README, convert `demo.mp4` to a `.gif` and replace the link above with:
> ```md
> ![Demo](assets/demo.gif)
> ```

---

## 🏗️ Model Architecture

The model is a `Sequential` network built on **Bidirectional LSTMs**. Each input verse is first passed through an **Embedding layer** (`output_dim=32`) that maps characters into dense vectors. The sequence then flows through **two stacked Bidirectional LSTM layers** (128 units each) — the first returns the full sequence, the second collapses it into a single representation — with **Layer Normalization** and **Dropout (0.3)** applied after each to stabilize training and reduce overfitting. Finally, a **Dense softmax layer** outputs a probability distribution over all meter classes.



---

## 📊 Dataset

Trained on the **Ashaar Dataset (أشعار)** — a curated collection of classical Arabic poetry for learning and evaluating Arabic poetic meters.

---

## 📈 Model Performance

Evaluated on a held-out test set:

<div align="center">

### 🏆 Test Accuracy: `94.96%`

</div>

The model reliably classifies Arabic poetic meters with high accuracy across diverse verse patterns and styles.

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/nashatfr/Buhoor.git
cd Buhoor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then open your browser, enter any Arabic verse, and see the predicted meter instantly.

---

## 📁 Project Structure

```
Buhoor/
├── app.py                 # Streamlit web app
├── requirements.txt       # Dependencies
├── assets/
│   └── demo.mp4           # Demo video
└── notebooks/             # Training notebook
```

---

<div align="center">

Built with care for the beauty of Arabic poetry

⋆ · ✦ · ⋆

</div>
