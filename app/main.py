from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas import Prediction_Response

from model.ml import predict_category

from .models import UserInput

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Premium prediction model"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=Prediction_Response)
def predict_premium(data: UserInput):
    try:
        prediction = predict_category(data)
        return JSONResponse(status_code=200, content={"predicted_category": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
