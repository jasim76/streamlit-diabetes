import pickle
import streamlit as st

#Membaca file .sav
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#Judul web
st.title ('Data Mining Prediksi Diabetes')

#bagi jadi 2 kolom
col1,col2 = st.columns(2)
with col1 :
    Pregnancies = st.text_input('Input Nilai Pregnancies')
    Glucose = st.text_input('Input Nilai Glucose')
    BloodPressure = st.text_input('Input Nilai BloodPressure')
    SkinThickness = st.text_input('Input Nilai SkinThickness')
with col2 :
    Insulin = st.text_input('Input Nilai Insulin')
    BMI = st.text_input('Input Nilai BMI')
    DiabetesPedigreeFunction = st.text_input('Input Nilai DiabetesPedigreeFunction')
    Age = st.text_input('Input Nilai Age')

#Code untuk prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button ('Tes Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if(diab_prediction[0]==1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diab_diagnosis)


