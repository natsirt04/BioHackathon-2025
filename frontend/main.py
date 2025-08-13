import streamlit as st
import requests

st.set_page_config(page_title="Cervical Cancer Risk Prediction", layout="wide")

st.title("🩺 Cervical Cancer Risk Prediction")

st.markdown(
    """
    Please fill out the form below.  
    All inputs are used to assess the risk prediction model for cervical cancer.
    """
)

with st.expander("👤 Personal Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.number_input("Age", min_value=0, step=1)
    with col2:
        Num_sex_partners = st.number_input("# Sexual Partners", min_value=0, step=1)
    with col3:
        First_sexual_intercourse = st.number_input("First Sexual Intercourse (age)", min_value=0, step=1)

    col4, col5 = st.columns(2)
    with col4:
        Num_pregnancies = st.number_input("# Pregnancies", min_value=0, step=1)
    with col5:
        Dx = st.selectbox("Diagnosis (Any)", (0, 1))


with st.expander("🚬 Smoking & Lifestyle"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Smokes = st.selectbox("Smokes", (0, 1))
    with col2:
        Smokes_years = st.number_input("Years Smoking", min_value=0.0, step=0.1)
    with col3:
        Smokes_packs_year = st.number_input("Packs/Year", min_value=0.0, step=0.1)

    col4, col5 = st.columns(2)
    with col4:
        Hormonal_contraceptives = st.selectbox("Hormonal Contraceptives", (0, 1))
    with col5:
        Hormonal_contraceptives_years = st.number_input("Years Used", min_value=0.0, step=0.1)

    col6, col7 = st.columns(2)
    with col6:
        IUD = st.selectbox("IUD", (0, 1))
    with col7:
        IUD_years = st.number_input("IUD Years", min_value=0.0, step=0.1)


with st.expander("🧬 STD History"):
    col1, col2, col3 = st.columns(3)
    with col1:
        STDs = st.selectbox("Any STD", (0, 1))
    with col2:
        STDs_number = st.number_input("Number of STDs", min_value=0, step=1)
    with col3:
        STDs_num_diagnosis = st.number_input("# of Diagnoses", min_value=0, step=1)

    col4, col5 = st.columns(2)
    with col4:
        STDs_time_since_first_diagnosis = st.number_input("Years Since First Diagnosis", min_value=0.0, step=0.1)
    with col5:
        STDs_time_since_last_diagnosis = st.number_input("Years Since Last Diagnosis", min_value=0.0, step=0.1)

    st.markdown("**Specific STDs:**")
    cols = st.columns(4)
    std_fields = [
        "STDs:condylomatosis",
        "STDs:cervical condylomatosis",
        "STDs:vaginal condylomatosis",
        "STDs:vulvo-perineal condylomatosis",
        "STDs:syphilis",
        "STDs:pelvic inflammatory disease",
        "STDs:genital herpes",
        "STDs:molluscum contagiosum",
        "STDs:AIDS",
        "STDs:HIV",
        "STDs:Hepatitis B",
        "STDs:HPV"
    ]
    std_values = {}
    for i, field in enumerate(std_fields):
        with cols[i % 4]:
            std_values[field] = st.selectbox(field, (0, 1))


with st.expander("🧪 Medical Tests & Diagnoses"):
    col1, col2, col3 = st.columns(3)
    with col1:
        Dx_Cancer = st.selectbox("Dx:Cancer", (0, 1))
    with col2:
        Dx_CIN = st.selectbox("Dx:CIN", (0, 1))
    with col3:
        Dx_HPV = st.selectbox("Dx:HPV", (0, 1))

    col4, col5, col6 = st.columns(3)
    with col4:
        Hinselmann = st.selectbox("Hinselmann Test", (0, 1))
    with col5:
        Schiller = st.selectbox("Schiller Test", (0, 1))
    with col6:
        Citology = st.selectbox("Cytology Test", (0, 1))


if st.button("🔍 Predict Risk"):
    features = [
        Age, Num_sex_partners, First_sexual_intercourse, Num_pregnancies,
        Smokes, Smokes_years, Smokes_packs_year, Hormonal_contraceptives,
        Hormonal_contraceptives_years, IUD, IUD_years, STDs, STDs_number,
        std_values["STDs:condylomatosis"], std_values["STDs:cervical condylomatosis"],
        std_values["STDs:vaginal condylomatosis"], std_values["STDs:vulvo-perineal condylomatosis"],
        std_values["STDs:syphilis"], std_values["STDs:pelvic inflammatory disease"],
        std_values["STDs:genital herpes"], std_values["STDs:molluscum contagiosum"],
        std_values["STDs:AIDS"], std_values["STDs:HIV"], std_values["STDs:Hepatitis B"],
        std_values["STDs:HPV"], STDs_num_diagnosis, STDs_time_since_first_diagnosis,
        STDs_time_since_last_diagnosis, Dx_Cancer, Dx_CIN, Dx_HPV, Dx,
        Hinselmann, Schiller, Citology
    ]

    response = requests.post(
        "http://localhost:8000/predict",
        json={"features": features}
    )
    if response.status_code == 200:
        result = response.json()["prediction"]
        st.success(f"Predicted Risk: {result}")
    else:
        st.error("Error getting prediction from backend.")
