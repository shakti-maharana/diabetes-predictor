# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 01:33:16 2025

@author: mahar
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("C:/Users/mahar/OneDrive/Desktop/Diabetes Prediction (Mini Project)/trained_model.sav", 'rb'))

# creating a function for Prediction
def diabetes_prediction(input):
    np_input = np.asarray(input)
    r_input = np_input.reshape(1,-1)
    prediction = loaded_model.predict(r_input)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    
    # giving a title
    st.title('🩺Diabetes Prediction Web App')
    
    st.markdown("🔹 **Model Accuracy** ≈ 78% ")
    
    st.subheader("📋 Feature Descriptions and Safe Ranges")

    st.markdown("""
                | Feature | Meaning | Safe/Normal Range |
                |--------|---------|--------------------|
                | Pregnancies | Number of times pregnant | N/A (used only for females) |
                | Glucose | Plasma glucose level (mg/dL) | Normal: < 140<br>Prediabetic: 140–199<br>Diabetic: ≥ 200 |
                | Blood Pressure | Diastolic BP (mm Hg) | Ideal: < 80 mm Hg |
                | Skin Thickness | Triceps skinfold thickness (mm) | Normal: 10–20 mm |
                | Insulin | 2-hour serum insulin (mu U/ml) | Normal: 16–166 |
                | BMI | Body Mass Index (kg/m²) | Normal: 18.5 – 24.9 |
                | Diabetes Pedigree Function | Hereditary diabetes risk | Lower is better (closer to 0) |
                | Age | Age in years | N/A, but age > 40 increases risk |
                """, unsafe_allow_html=True)
    
    # getting the input data from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    # code for Prediction
    diagnosis = ''  # empty string
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
    
    if 'not diabetic' in diagnosis.lower():
        st.info("🛡 *Tips to stay non-diabetic:*\n"
            "- Maintain a healthy diet (low sugar, high fiber)\n"
            "- Exercise regularly (30 mins/day)\n"
            "- Keep your weight in check\n"
            "- Avoid smoking and limit alcohol\n"
            "- Get regular checkups if you have family history")
    elif 'diabetic' in diagnosis.lower():
        st.warning("📋 *Daily tips for managing diabetes:*\n"
               "- Eat balanced meals (low carbs, high fiber)\n"
               "- Monitor your blood sugar levels\n"
               "- Take medications/insulin as prescribed\n"
               "- Exercise regularly (walk/yoga)\n"
               "- Get 6–8 hrs of sleep & manage stress\n"
               "- Regularly consult your doctor")
    
    st.markdown("---")
    st.markdown("💻 Made by **Shakti* and *Sanjana ❤", unsafe_allow_html=True)

      
if __name__ == '__main__':
    main()
    