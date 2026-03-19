import streamlit as st # type: ignore
import pandas as pd
import joblib

model = joblib.load("df.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction detales and use the predict button")

st.divider()

transaction_type = st.selectbox("Transcantion Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])

amount = st.numer_input("Amount", min_value = 0.0, value = 1000.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)", min_values = 0.0, value =10000.0 )

newbalanceOrig = st.number_input("New Balance (Sender)",min_value = 0.0, value = 9000.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value =0.0, value = 0.0 )

newbalanceDest = st.number_input("New Balance (Receiver)", min_value =0.0, value = 0.0 )

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data[0])

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be a fraud")
    else:
        st.success("This transcation looks like it's not a fraud")

