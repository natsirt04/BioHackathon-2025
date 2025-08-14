from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

try:
    with open("xgboost_model_v1.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Model file not found!")
    model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI()

class PatientData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: PatientData):
    if model is None:
        return {"error": "Model not loaded"}
    try:
        prediction = model.predict([np.array(data.features)])
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

