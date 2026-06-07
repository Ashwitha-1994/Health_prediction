# Health_prediction
Health Prediction Application built using Python, Streamlit, SQLite, and Machine Learning. The application supports CRUD operations for patient records, validates user input, predicts health risk levels based on blood test parameters (Glucose, Haemoglobin, Cholesterol), and automatically generates AI-powered health remarks.
# Health Prediction Application

## Overview

The Health Prediction Application is a machine learning-powered healthcare management system developed using Python, Streamlit, SQLite, and Scikit-learn. The application allows users to manage patient records and predict health risk levels based on blood test parameters such as Glucose, Haemoglobin, and Cholesterol.

## Features

* Create, Read, Update, and Delete (CRUD) patient records
* User-friendly Streamlit interface
* Input validation for email, date of birth, and numeric health parameters
* SQLite database for persistent storage
* Machine Learning-based health risk prediction
* Automatic AI-generated remarks (Low Risk, Medium Risk, High Risk)
* Real-time prediction results displayed within the application

## Technology Stack

* Python
* Streamlit
* SQLite
* Pandas
* Scikit-learn
* Joblib

## Machine Learning Model

A Random Forest Classifier was trained on a healthcare dataset containing Glucose, Haemoglobin, and Cholesterol values. The model predicts the patient's health risk level and generates remarks automatically.

## Database Schema

* Patient ID
* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks (Generated from AI)

## Application Workflow

1. User enters patient details.
2. Data validation is performed.
3. The trained ML model predicts the risk level.
4. Prediction is stored in the Remarks field.
5. Patient data is saved in SQLite.
6. Users can view, update, or delete records.

## Future Enhancements

* Integration with external healthcare APIs
* User authentication and role-based access
* Dashboard analytics and visualization
* Deployment on Streamlit Cloud or AWS

## Author

Ashwitha K K
Data Science Graduate (GUVI-HCL)

