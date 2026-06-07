import joblib
import pandas as pd

model = joblib.load(r"D:\Projects\Health_Risk_Project\health_model.pkl")

def predict_risk(glucose,haemoglobin,cholesterol):

    data = pd.DataFrame([{
        'glucose':glucose,
        'haemoglobin':haemoglobin,
        'cholesterol':cholesterol
    }])

    prediction = model.predict(data)

    return prediction[0]
