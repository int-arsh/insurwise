from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .models import UserInput
from  .ml import predict_category

app = FastAPI()

@app.get('/')
def home():
    return {'message': "Premium prediction model"}

@app.get('/health')
def health():
    return {
        "status": "ok"
    }

@app.post('/predict')
def predict_premium(data: UserInput):
    prediction = predict_category(data)
    return JSONResponse(status_code=200, content={'predicted_category': prediction})





