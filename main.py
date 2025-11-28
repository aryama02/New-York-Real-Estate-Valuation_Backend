from fastapi import FastAPI
import uvicorn
from schema import predict_input
import pickle
import numpy as np

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home_page():
    return {"AppName": "House Price Prediction Server", "Version": "1.0.0"}


@app.post("/predict-price")
async def predict_price(data: predict_input):
    ip_data = np.array([data.BathroomsFull, data.BathroomsHalf, data.BedroomsTotal, data.LivingArea])
    predicted_price = model.predict(ip_data.reshape(1, -1))[0]
    return {"predicted_price": float(predicted_price)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
