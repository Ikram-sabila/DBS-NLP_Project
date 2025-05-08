# 🧠 Sentiment Analysis of Livin' by Mandiri User Reviews using LSTM

Proyek ini merupakan analisis sentimen terhadap ulasan pengguna aplikasi **Livin' by Mandiri** menggunakan teknik **Natural Language Processing (NLP)** dan model **Long Short-Term Memory (LSTM)**. Tujuannya adalah untuk mengklasifikasikan sentimen pengguna ke dalam beberapa kategori seperti *positif*, *netral*, dan *negatif* berdasarkan teks ulasan mereka.

---

## 📌 Fitur Utama

- Preprocessing data teks (cleaning, tokenization, padding)
- Word embedding menggunakan Tokenizer Keras
- Arsitektur Deep Learning menggunakan LSTM
- Evaluasi model dengan metrik akurasi, precision, recall, dan confusion matrix
- Visualisasi hasil prediksi

---

## 🛠️ Teknologi yang Digunakan

- Python
- TensorFlow / Keras
- Pandas & Numpy
- Matplotlib & Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 🧪 Arsitektur Model

Model dibangun dengan arsitektur:

- Embedding Layer
- LSTM Layer
- Dropout
- Dense Output Layer 

---

## 🗃️ Dataset

Dataset berisi ulasan pengguna aplikasi **Livin' by Mandiri** yang dikumpulkan secara manual/otomatis dari Google Play Store. Label sentimen dikategorikan sebagai:
- `0`: Negatif
- `1`: Netral
- `2`: Positif

---

## 🚀 Cara Menjalankan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/Ikram-sabila/DBS-NLP_Project.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Jalankan notebook:
   ```bash
   jupyter notebook

4. Buka file notebook utama (model.ipynb) dan jalankan sel secara berurutan.
