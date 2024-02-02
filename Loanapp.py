import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

model = joblib.load('nbc.pkl') 
x_label_encoder = joblib.load('labelencoder_x.pkl')  
scaler = joblib.load('scaler.pkl')
# Streamlit app
st.title('Loan Approval Predictor')

# Centered input widgets
st.header('Input Features')

gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
dependents = st.slider('Dependents', 0, 3, 1)
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income', min_value=0)
coapplicant_income = st.number_input('Coapplicant Income', min_value=0)
loan_amount = st.number_input('Loan Amount', min_value=0)
loan_amount_term = st.number_input('Loan Amount Term', min_value=0)
credit_history = st.selectbox('Credit History', [0, 1])
property_area = st.selectbox('Property Area', ['Urban', 'Rural', 'Semiurban'])

# Make prediction
input_data = {
    'Gender': [le.transform([gender])[0]],
    'Married': [le.transform([married])[0]],
    'Dependents': [dependents],
    'Education': [le.transform([education])[0]],
    'Self_Employed': [le.transform([self_employed])[0]],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_amount_term],
    'Credit_History': [credit_history],
    'Property_Area': [le.transform([property_area])[0]]
}

input_df = pd.DataFrame(input_data)

prediction = nbc.predict(input_df)[0]

# Display the result
st.header('Prediction Result')
st.write(f'The model predicts that the loan status is: {le.inverse_transform([prediction])[0]}')
st.write(f'Model Accuracy: {accuracy:.2%}')
