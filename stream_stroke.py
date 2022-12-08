import pickle
import numpy as np
import streamlit as st
# load save model
model = pickle.load(open('penyakit_stroke.sav','rb'))


# judul web 
st.title ('prediksi penyakit stroke')
st.title ('ARID HASAN 191351006 MALAM A')

col1, col2, col3 = st.columns(3)

with col1:
    id = st.number_input('id')
with col2:
    gender = st.number_input('jenis kelamin')
with col3:
    age = st.number_input('umur')
with col1:
    hypertension = st.number_input('tekanan darah')
with col2:
    heart_disease = st.number_input('penyakit jantung')
with col3:
    ever_married = st.number_input('setatus menikah')
with col1:
    work_type = st.number_input('tipe pekerjaan')
with col2:
    Residence_type = st.number_input('residence')
with col3:
    avg_glucose_level = st.number_input('kadar gula')
with col1:
    bmi = st.number_input('body mas index')
with col2:
    smoking_status = st.number_input('status perokok')


stroke_diagnosis =''

if st.button('prediksi penyakit stroke'):
    stroke_prediction = model.predict([[id,gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])

    if (stroke_prediction[0]==1):
        stroke_diagnosis = 'pasien terkena penyakit STROKE'
    else:
        stroke_diagnosis = 'pasien tidak penyakit STROKE'
    st.success(stroke_diagnosis)