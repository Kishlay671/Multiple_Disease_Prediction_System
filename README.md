### Multiple Disease Prediction System
# Project Overview

The Multiple Disease Prediction System is a web-based application built using Streamlit that allows users to predict the likelihood of various diseases based on their medical parameters. Currently, the system supports prediction for:

1)Diabetes

2)Heart Disease

3)Parkinson’s Disease

The system is designed to be extensible, so additional diseases can be added in the future with ease.

## Features

User-friendly web interface with 3-column input layout for cleaner UI.

Predicts disease likelihood based on user input using pre-trained Machine Learning models.

Real-time predictions using Streamlit.

Handles input validation to ensure numeric values are provided.

Modular design to add new diseases easily.

## Project Structure 
Multiple_Disease_Prediction_System/
│
├── Models/                # Pre-trained ML models (.sav files)
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│   └── parkinsons_model.sav
│
├── Multiple_Disease_Prediction.py   # Streamlit app
├── requirements.txt       # Python dependencies
└── README.md

## Technologies Used

Python 3.11.13

Streamlit – for building the web interface

scikit-learn – for ML model loading and predictions

Pickle – for saving and loading pre-trained ML models

Pandas & NumPy – for data handling

## Future Updates

The system is designed to be extensible, and future updates may include prediction for additional diseases such as:
# Kidney Disease
# Liver Disease
# COVID-19 severity prediction
