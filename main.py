from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import json

app = FastAPI()

with open("bangalore_home_prices_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

class HouseFeatures(BaseModel):
    total_sqft: float
    bath: int
    bhk: int
    location: str

@app.post("/predict")
def predict_price(data: HouseFeatures):
    try:
        loc_index = data_columns.index(data.location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = data.total_sqft
    x[1] = data.bath
    x[2] = data.bhk
    if loc_index >= 0:
        x[loc_index] = 1

    prediction = round(model.predict([x])[0], 2)
    return {"estimated_price_lakhs": prediction}
