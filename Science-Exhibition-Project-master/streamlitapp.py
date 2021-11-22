import streamlit as st
from utils import *

# html_temp = """
# <div style="background-color:yellow;padding:13px">
# <h2 style="color:blue">Streamlit Loan Prediction ML App</h2>
# </div>
# """

age = st.sidebar.slider("Age", 0, 100)
anaemia = st.sidebar.slider("Anaemia", 0, 1)
creatinine_phosphokinase = st.number_input("Creatinine phosphokinase")
diabetes = st.sidebar.slider("Diabetes", 0, 1)
ejection_fraction = st.number_input("Ejection fraction")
high_blood_pressure = st.sidebar.slider("High blood pressure", 0, 1)
platelets = st.number_input("Platelets")
serum_creatinine = st.number_input("Serum creatinine")
serum_sodium = st.number_input("Serum sodium")
sex = st.sidebar.slider("Sex", 0, 1)
smoking = st.sidebar.slider("Smoking", 0, 1)
time = st.number_input("Time")
results = ""

if st.button("Predict"):
    result = preprocessdata(
        age,
        anaemia,
        creatinine_phosphokinase,
        diabetes,
        ejection_fraction,
        high_blood_pressure,
        platelets,
        serum_creatinine,
        serum_sodium,
        sex,
        smoking,
        time,
    )
    st.success(result)
    print(result)
