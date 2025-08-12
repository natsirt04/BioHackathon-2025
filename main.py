import streamlit as st
import math

st.header("Cervical Cancer Risk Prediction")

# Dataset columns (excluding Biopsy)
col1, col2, col3 = st.columns(3)
with col1:
    Age = st.number_input("Age", min_value=0, step=1)
with col2:
    Num_sex_partners = st.number_input("Number of sexual partners", min_value=0, step=1)
with col3:
    First_sexual_intercourse = st.number_input("First sexual intercourse (age)", min_value=0, step=1)

col4, col5, col6 = st.columns(3)
with col4:
    Num_pregnancies = st.number_input("Number of pregnancies", min_value=0, step=1)
with col5:
    Smokes = st.selectbox("Smokes", (0, 1))
with col6:
    Smokes_years = st.number_input("Smokes (years)", min_value=0.0, step=0.1)

col7, col8, col9 = st.columns(3)
with col7:
    Smokes_packs_year = st.number_input("Smokes (packs/year)", min_value=0.0, step=0.1)
with col8:
    Hormonal_contraceptives = st.selectbox("Hormonal Contraceptives", (0, 1))
with col9:
    Hormonal_contraceptives_years = st.number_input("Hormonal Contraceptives (years)", min_value=0.0, step=0.1)

col10, col11, col12 = st.columns(3)
with col10:
    IUD = st.selectbox("IUD", (0, 1))
with col11:
    IUD_years = st.number_input("IUD (years)", min_value=0.0, step=0.1)
with col12:
    STDs = st.selectbox("STDs", (0, 1))

col13, col14, col15 = st.columns(3)
with col13:
    STDs_number = st.number_input("STDs (number)", min_value=0, step=1)
with col14:
    STDs_condylomatosis = st.selectbox("STDs:condylomatosis", (0, 1))
with col15:
    STDs_cervical_condylomatosis = st.selectbox("STDs:cervical condylomatosis", (0, 1))

col16, col17, col18 = st.columns(3)
with col16:
    STDs_vaginal_condylomatosis = st.selectbox("STDs:vaginal condylomatosis", (0, 1))
with col17:
    STDs_vulvo_perineal_condylomatosis = st.selectbox("STDs:vulvo-perineal condylomatosis", (0, 1))
with col18:
    STDs_syphilis = st.selectbox("STDs:syphilis", (0, 1))

col19, col20, col21 = st.columns(3)
with col19:
    STDs_pelvic_inflammatory_disease = st.selectbox("STDs:pelvic inflammatory disease", (0, 1))
with col20:
    STDs_genital_herpes = st.selectbox("STDs:genital herpes", (0, 1))
with col21:
    STDs_molluscum_contagiosum = st.selectbox("STDs:molluscum contagiosum", (0, 1))

col22, col23, col24 = st.columns(3)
with col22:
    STDs_AIDS = st.selectbox("STDs:AIDS", (0, 1))
with col23:
    STDs_HIV = st.selectbox("STDs:HIV", (0, 1))
with col24:
    STDs_Hepatitis_B = st.selectbox("STDs:Hepatitis B", (0, 1))

col25, col26, col27 = st.columns(3)
with col25:
    STDs_HPV = st.selectbox("STDs:HPV", (0, 1))
with col26:
    STDs_num_diagnosis = st.number_input("STDs: Number of diagnosis", min_value=0, step=1)
with col27:
    STDs_time_since_first_diagnosis = st.number_input("STDs: Time since first diagnosis", min_value=0.0, step=0.1)

col28, col29, col30 = st.columns(3)
with col28:
    STDs_time_since_last_diagnosis = st.number_input("STDs: Time since last diagnosis", min_value=0.0, step=0.1)
with col29:
    Dx_Cancer = st.selectbox("Dx:Cancer", (0, 1))
with col30:
    Dx_CIN = st.selectbox("Dx:CIN", (0, 1))

col31, col32, col33 = st.columns(3)
with col31:
    Dx_HPV = st.selectbox("Dx:HPV", (0, 1))
with col32:
    Dx = st.selectbox("Dx", (0, 1))
with col33:
    Hinselmann = st.selectbox("Hinselmann", (0, 1))

col34, col35, _ = st.columns(3)
with col34:
    Schiller = st.selectbox("Schiller", (0, 1))
with col35:
    Citology = st.selectbox("Citology", (0, 1))

if st.button("Submit"):
    st.write("Prediction logic to be added once the model is trained.")
