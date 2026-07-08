# 🐾 AI Pet Face Classification

An AI-powered web application that classifies pet images into five different categories using Deep Learning. The application allows users to upload a pet image or capture one using their camera and instantly predicts the pet type with a confidence score.

---

## 📌 Project Overview

The **AI Pet Face Classification** system is built using **TensorFlow**, **MobileNetV2**, and **Streamlit**. It uses a pre-trained deep learning model (Transfer Learning) to recognize different pet faces and provide fast, accurate predictions through a simple and user-friendly web interface.

---

## ✨ Features

- 🐾 Classifies 5 different pet categories
- 📁 Upload pet images
- 📷 Capture live photos using the device camera
- 🤖 AI-powered image classification
- 🎯 Confidence score for each prediction
- 🏆 Top 3 similar match predictions
- 📊 Prediction probability display
- 📱 Responsive and user-friendly interface
- ⚡ Fast real-time predictions

---

## 🐾 Supported Pets

- 🐱 Cat
- 🐶 Dog
- 🦦 Ferret
- 🐹 Hamster
- 🐰 Rabbit

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- MobileNetV2
- Streamlit
- NumPy
- Pandas
- Pillow

---

## 📂 Project Structure

```text
Pet-Face-Classification/
│── app.py
│── pet_classifier.keras
│── class_names.pkl
│── requirements.txt
│── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Pet-Face-Classification.git
```

Go to the project folder:

```bash
cd Pet-Face-Classification
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 How to Use

1. Open the Streamlit application.
2. Choose one of the following options:
   - 📁 Upload Image
   - 📷 Take Photo
3. Upload or capture a pet image.
4. Click **Predict Pet**.
5. View:
   - Predicted pet
   - Confidence score
   - Top similar matches
   - Pet information

---

## 🎯 Model Information

- Model: MobileNetV2 (Transfer Learning)
- Framework: TensorFlow / Keras
- Input Image Size: 224 × 224 pixels
- Number of Classes: 5

---

## 📊 Project Workflow

1. Dataset Collection
2. Image Preprocessing
3. Transfer Learning using MobileNetV2
4. Model Training
5. Model Evaluation
6. Save Trained Model
7. Streamlit Web Application
8. GitHub Deployment
9. Streamlit Cloud Deployment

---

## 💡 Future Improvements

- Support more pet species
- Breed-level classification
- Real-time video prediction
- Downloadable prediction report
- Prediction history
- Multi-language support

---

## 👨‍💻 Developer

**K. Rakesh Reddy**

B.Tech – Computer Science & Engineering

---

## 📄 License

This project is developed for educational and portfolio purposes.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
