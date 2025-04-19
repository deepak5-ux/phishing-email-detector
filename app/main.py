from fastapi import FastAPI, HTTPException, Request, Header, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import joblib
import os
from dotenv import load_dotenv
from utils.text_cleaning import clean_text
from utils.logger import setup_logger

# Load .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Set up logger
logger = setup_logger()

# Auth scheme for Swagger
security = HTTPBearer()

# Load model/vectorizer
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "phishing_rf_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")
rf_model = joblib.load(model_path)
tfidf_vectorizer = joblib.load(vectorizer_path)

# FastAPI app
app = FastAPI(title="Phishing Email Detection API")

# Input model
class EmailInput(BaseModel):
    text: str

# Root
@app.get("/")
def read_root():
    return {"message": "Phishing Detection API is running 🚀"}

# Predict route with Swagger auth
@app.post("/predict")
def predict_phishing(
    input: EmailInput,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    request: Request = None
):
    token = credentials.credentials
    if token != API_TOKEN:
        logger.warning(f"Unauthorized access from {request.client.host}")
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        cleaned = clean_text(input.text)
        vectorized = tfidf_vectorizer.transform([cleaned])
        prediction = rf_model.predict(vectorized)[0]
        result = "Phishing Email 🚨" if prediction == 1 else "Safe Email ✅"
        logger.info(f"Prediction: {result} | From: {request.client.host}")
        return {"prediction": result}
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
