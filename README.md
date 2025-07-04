# 🏠 Bangalore House Price Prediction

This project predicts real estate prices in Bangalore using a trained ML model, FastAPI for backend, and Streamlit for UI.

## 📦 Features
- Predicts price based on total sqft, BHK, bath, and location
- REST API built with FastAPI
- Interactive UI built using Streamlit

## 🚀 How to Run

### 1. Backend (FastAPI)
```bash
cd backend
uvicorn main:app --reload
```

### 2. Frontend (Streamlit)
Open a new terminal:
```bash
cd frontend
streamlit run app.py
```

## 📂 Folder Structure
```
bangalore_price_predictor/
├── backend/
│   ├── main.py
│   ├── bangalore_home_prices_model.pkl
│   └── columns.json
├── frontend/
│   └── app.py
├── requirements.txt
└── README.md
```
