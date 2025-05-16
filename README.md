
# 🎭 Emotion Detector - by Fixar (Zulfikar Sandira)

Deteksi emosi wajah secara real-time menggunakan Python, OpenCV, dan DeepFace.

---

## 🔧 Requirement

### Python:
- Rekomendasi: Python **3.8 - 3.11**
- Jangan pakai Python 3.12 ke atas (banyak package belum support)

### Module:
```
opencv-python  
deepface  
tensorflow==2.12.0  
tf-keras  
```

---

## ⚙️ Cara Instalasi (1x Jalan, Gak Ribet)

### 1. Clone Repo
```bash
git clone https://github.com/jaa2006/emotion-detector.git
cd emotion-detector
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate         # Windows
```

### 3. Install Semua Modul
```bash
pip install -r requirements.txt
```

Kalau error soal TensorFlow versi:
```bash
pip install tensorflow==2.12.0
pip install tf-keras
```

---

## ▶️ Cara Menjalankan Program

### Run manual:
```bash
python "emotion detektor.py"
```

### Run lewat .bat (Windows Only):
Buat file `run.bat` isi:
```bat
@echo off
venv\Scripts\activate
python "emotion detektor.py"
pause
```

Tinggal **double click `run.bat`** buat jalanin.

---

## 🧠 Deteksi Emosi yang Didukung

- Angry  
- Happy  
- Sad  
- Surprise  
- Neutral  
- Fear  
- Disgust  

---

## 🧑‍💻 Developer

**Zulfikar Sandira (FIXCODE TEAM)**  
Email: gamingdzul5@gmail.com  
GitHub: https://github.com/jaa2006

---

## 🐍 requirements.txt (isi file ini juga di repo lo)

```txt
opencv-python  
deepface  
tensorflow==2.12.0  
tf-keras  
```

---

## 🖇 Remote GitHub (kalau belum diset)

```bash
git remote add origin https://github.com/jaa2006/emotion-detector.git
```

---

## 🪪 Lisensi

MIT License — Bebas pakai, modif, asal tetap cantumkan nama pembuat asli.
