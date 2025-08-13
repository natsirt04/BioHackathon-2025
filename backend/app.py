from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

model = pickle.load(open("test.pkl", "rb"))

app = FastAPI()

class PatientData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: PatientData):
    prediction = model.predict([np.array(data.features)])
    return {"prediction": int(prediction[0])}
