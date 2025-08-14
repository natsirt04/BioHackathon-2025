import streamlit as st
import requests

st.set_page_config(page_title="Cervical Cancer Risk Prediction", layout="wide")

st.title("🩺 Cervical Cancer Risk Prediction")

st.markdown(
    """
    Please fill out the form below.  
    Inputs are limited to the top 10 most important features for prediction.
    """
)

col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input("Age", min_value=0, step=1)
with col2:
    Hormonal_contraceptives = st.selectbox("Hormonal Contraceptives", (0, 1))
with col3:
    IUD = st.selectbox("IUD", (0, 1))

col4, col5, col6 = st.columns(3)
with col4:
    Schiller = st.selectbox("Schiller Test", (0, 1))
with col5:
    Hinselmann = st.selectbox("Hinselmann Test", (0, 1))
with col6:
    Citology = st.selectbox("Cytology Test", (0, 1))

col7, col8 = st.columns(2)
with col7:
    STDs_number = st.number_input("Number of STDs", min_value=0, step=1)
with col8:
    STDs = st.selectbox("Any STD", (0, 1))

col9, col10 = st.columns(2)
with col9:
    STDs_condylomatosis = st.selectbox("STDs:condylomatosis", (0, 1))
with col10:
    STDs_HIV = st.selectbox("STDs:HIV", (0, 1))

if st.button("🔍 Predict Risk"):
    features = [
        Schiller, Age, Hormonal_contraceptives, Hinselmann,
        STDs_number, STDs, IUD, Citology, STDs_condylomatosis, STDs_HIV
    ]

    response = requests.post(
        "http://backend:8000/predict",
        json={"features": features}
    )
    if response.status_code == 200:
        result = response.json().get('prediction')
        
        if result == 0:
            st.success("Predicted Risk: Low ✅")
            st.info("Your risk is low, but regular checkups are recommended.")
        elif result == 1:
            st.warning("Predicted Risk: High ⚠️")
            st.error("Warning: Please visit a hospital for a medical checkup.")
        else:
            st.error(f"Unexpected prediction value: {result}")
    else:
        st.error("Error getting prediction from backend.")
