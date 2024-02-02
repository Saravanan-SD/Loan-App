import streamlit as st

st.title('Loan Approval Predictor')

# Sidebar with input widgets
st.sidebar.header('Input Features')
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
married = st.sidebar.selectbox('Married', ['Yes', 'No'])
dependents = st.sidebar.slider('Dependents', 0, 3, 1)
education = st.sidebar.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.sidebar.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.sidebar.number_input('Applicant Income', min_value=0)
coapplicant_income = st.sidebar.number_input('Coapplicant Income', min_value=0)
loan_amount = st.sidebar.number_input('Loan Amount', min_value=0)
loan_amount_term = st.sidebar.number_input('Loan Amount Term', min_value=0)
credit_history = st.sidebar.selectbox('Credit History', [0, 1])
property_area = st.sidebar.selectbox('Property Area', ['Urban', 'Rural', 'Semiurban'])