# utils.py

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def load_model_and_scaler():
    model = joblib.load('./model/titanic_model.pkl')
    scaler = joblib.load('./model/scaler.pkl')
    return model, scaler

def preprocess_input(input_data, scaler):
    input_df = pd.DataFrame([input_data])
    input_df_scaled = scaler.transform(input_df)
    return input_df_scaled

def predict_survival(input_data):
    model, scaler = load_model_and_scaler()
    input_df_scaled = preprocess_input(input_data, scaler)
    prediction = model.predict(input_df_scaled)
    return 'Survived' if prediction[0] == 1 else 'Did Not Survive'