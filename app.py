import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load('churn_model_pipeline.pkl')

# Set the title and a description
st.title('Customer Churn Prediction 🔮')
st.write('This app predicts if a customer is likely to churn based on their account information. Please provide the customer details in the sidebar.')

# --- Sidebar for User Input ---
st.sidebar.header('Customer Account Details')

# Create input fields in the sidebar
# NOTE: The options here should match the data your model was trained on
# For example, if your 'Contract' column had 'Month-to-month', 'One year', 'Two year'
contract = st.sidebar.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
internet_service = st.sidebar.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
payment_method = st.sidebar.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
tenure = st.sidebar.slider('Tenure (Months)', 1, 72, 24)
monthly_charges = st.sidebar.slider('Monthly Charges ($)', 18.0, 120.0, 60.0)
total_charges = st.sidebar.slider('Total Charges ($)', 18.0, 9000.0, 1500.0)

# The other features can be simplified for this demo
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.sidebar.selectbox('Senior Citizen', ['No', 'Yes'])
partner = st.sidebar.selectbox('Partner', ['No', 'Yes'])
dependents = st.sidebar.selectbox('Dependents', ['No', 'Yes'])
phone_service = st.sidebar.selectbox('Phone Service', ['No', 'Yes'])
multiple_lines = st.sidebar.selectbox('Multiple Lines', ['No', 'Yes', 'No phone service'])
online_security = st.sidebar.selectbox('Online Security', ['No', 'Yes', 'No internet service'])

# --- Prediction Logic ---
if st.sidebar.button('Predict Churn'):
    # Create a DataFrame from the user inputs
    # The column names MUST match the names used during model training
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [1 if senior_citizen == 'Yes' else 0], # Needs to be numeric
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'PhoneService': [phone_service],
        'MultipleLines': [multiple_lines],
        'InternetService': [internet_service],
        'OnlineSecurity': [online_security],
        # Add the remaining features your model expects with dummy values if needed
        'OnlineBackup': ['No'],
        'DeviceProtection': ['No'],
        'TechSupport': ['No'],
        'StreamingTV': ['No'],
        'StreamingMovies': ['No'],
        'Contract': [contract],
        'PaperlessBilling': ['Yes'],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })

    # Make prediction
    prediction_proba = model.predict_proba(input_data)[:, 1] # Probability of 'Churn'
    churn_probability = prediction_proba[0]

    # Display result
    st.subheader('Prediction Result')
    if churn_probability > 0.5:
        st.error(f'High Churn Risk: {churn_probability:.2%}')
        st.write('This customer is likely to churn. Consider taking retention actions.')
    else:
        st.success(f'Low Churn Risk: {churn_probability:.2%}')
        st.write('This customer is likely to stay.')