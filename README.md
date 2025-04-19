# 📧 Phishing Email Detection API

An AI-powered REST API built with FastAPI that detects whether an email is a phishing attempt or safe using a trained Machine Learning model. This project is containerized using Docker and ready for deployment on platforms like Render or AWS.

---

## 🚀 Features

- **FastAPI-powered REST API** with Swagger (OpenAPI) documentation
- **Text Preprocessing Pipeline** with NLTK for cleaning email content
- **ML Model Integration**: Random Forest trained on TF-IDF features
- **Secure API** using Bearer Token authentication
- **Detailed Logging** with timestamp, IP tracking, and prediction logs
- **Dockerized** for consistent local and production environments
- **Fully Tested** using `pytest` for API endpoint validation

---

## 🛠️ Tech Stack

- **FastAPI** for building the REST API
- **scikit-learn** and **joblib** for the ML model
- **NLTK** for text preprocessing
- **Docker** for containerization
- **Render** (or AWS) for deployment
- **pytest** for automated testing

---

## 🧪 Input Example

Send a POST request to `/predict` with a JSON body:

```json
{
  "text": "Congratulations! You've won a free iPhone. Click here."
}
```

If the token is valid, you'll get a prediction:

```json
{
  "prediction": "Phishing Email 🚨"
}
```

---

## 📂 Project Structure

```
phishing_email_detector/
├── app/
│   └── main.py               # FastAPI app
├── utils/
│   ├── text_cleaning.py     # Preprocessing
│   └── logger.py            # Logger setup
├── model/
│   ├── phishing_rf_model.pkl
│   └── tfidf_vectorizer.pkl
├── tests/
│   └── test_main.py         # Pytest-based tests
├── logs/
│   └── app.log              # Auto-generated logs
├── .env                     # Environment variables
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker setup
└── README.md
```

---

## ⚙️ Installation

### 📌 Prerequisites

- Python 3.9+
- Docker
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/phishing-email-detector.git
cd phishing-email-detector
```

### 2. Set Up Environment
Create a `.env` file:
```bash
API_TOKEN=your-secret-token
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
uvicorn app.main:app --reload
```
Go to `http://127.0.0.1:8000/docs` to explore the Swagger UI.

---

## 🧪 Testing

Run unit tests using:
```bash
pytest tests/
```

---

## 🐳 Docker Usage

### Build the Docker Image
```bash
docker build -t phishing-detector .
```

### Run the Container
```bash
docker run --name phishing-api -p 8000:8000 --env-file .env phishing-detector
```

Visit `http://localhost:8000/docs` to test it in Swagger.

---

## ☁️ Deploy to Render

### 1. Push Code to GitHub
Ensure your repo is pushed to GitHub.

### 2. Create a New Render Web Service
- Go to [Render](https://render.com/)
- Select "New Web Service"
- Connect to your GitHub repo
- Choose environment: **Docker**
- Set your environment variables (API_TOKEN)

### 3. Deploy
Render will build and deploy your app. Use the provided Render URL to access Swagger.

---

## 🔐 API Authentication

Use the **Authorize 🔒** button in Swagger to test:
```text
Bearer your-secret-token
```

You can also test using Postman with the Authorization header:
```
Key: Authorization
Value: Bearer your-secret-token
```

---

## 📝 Logs

Logs are saved under `/logs/app.log`. Example entry:
```
2025-04-19 10:45:00 - INFO - Prediction: Phishing Email 🚨 | From: 127.0.0.1
```

---

## 🧠 Skills Demonstrated Through This Project

- ✅ Demonstrates **End-to-End ML Integration**
- ✅ Implements **Authentication & Logging**
- ✅ Shows **MLOps practices** (Docker, testing, deployment)
- ✅ Easy to demo with Swagger UI & Postman

---

## 🤝 Contributing
Feel free to fork and enhance. PRs are welcome!

---

## 📧 Contact
**Deepak B**  
[LinkedIn](www.linkedin.com/in/deepak511) | deepakbalraj511@gmail.com
