import streamlit as st
import json
import requests

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]
    locations = [col.title() for col in data_columns[3:]]

st.title("🏠 Bangalore House Price Predictor")

location = st.selectbox("Location", sorted(locations))
total_sqft = st.number_input("Total Square Feet", min_value=300.0, max_value=10000.0, step=50.0)
bath = st.slider("Number of Bathrooms", 1, 5, 2)
bhk = st.slider("Number of Bedrooms (BHK)", 1, 5, 2)

if st.button("Predict Price"):
    payload = {
        "total_sqft": total_sqft,
        "bath": bath,
        "bhk": bhk,
        "location": location
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        st.success(f"💰 Estimated Price: ₹ {result['estimated_price_lakhs']} Lakhs")
    except:
        st.error("⚠️ Could not connect to the FastAPI server. Make sure it's running.")
