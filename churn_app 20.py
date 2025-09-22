import pandas as pd
import streamlit as st
import joblib
import os


model_path = "churn_piprline.pkl"

if os.path.exists(model_path):
    pipeline = joblib.load(model_path)
    st.success("Model load successful")
else:
    st.warning(f'Model file {model_path} does not exist')

    st.title("Customer Churn Predictiction")
    st.write("Fill your details")



# App Heading
st.title('Customer Churn Prediction')
st.write('Fill Your Details')
# Form inputs
with st.form('Churn_Form'):
    gender = st.selectbox('Gender', ['Male', 'Female'])
    SeniorCitizen = st.selectbox('SeniorCitizen', ['No', 'Yes'])
    Partner = st.selectbox('Partner', ['Yes', 'No'])
    Dependents = st.selectbox('Dependents', ['Yes', 'No'])
    Tenure = st.number_input('Tenure (In Months)', min_value= 0)
    PhoneService = st.selectbox('PhoneService', ['Yes', 'No'])
    MultipleLines = st.selectbox('MultipleLines', ['Yes', 'No'])
    InternetService = st.selectbox('InternetService', ['DSL','Fiber optic' 'No'])
    OnlineSecurity = st.selectbox('OnlineSecurity', ['No', 'No internet service' 'Yes'])
    OnlineBackup = st.selectbox('OnlineBackup', ['No', 'No internet service' 'Yes'])
    DeviceProtection = st.selectbox('DeviceProtection', ['No', 'No internet service' 'Yes'])
    TechSupport = st.selectbox('TechSupport', ['No', 'No internet service' 'Yes'])
    StreamingTV = st.selectbox('StreamingTV', ['No', 'No internet service' 'Yes'])
    StreamingMovies = st.selectbox('StreamingMovies', ['No', 'No internet service' 'Yes'])
    Contracts = st.selectbox('Contracts', ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.selectbox('PaperlessBilling', ['Yes', 'No'])
    PaymentMethod = st.selectbox('PaymentMethod', ['Bank Transfer (automatic)', 'Credit card (automatic)', 'Electronic cheque', 'Mail cheques', ])
    MonthlyCharges = st.number_input('MonthlyCharges', min_value= 0.0)
    TotalCharges= st.number_input('TotalCharges', min_value= 0.0)

    submitted = st.form_submit_button('Predict')