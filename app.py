#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 01:20:27 2025

@author: kishlaykumar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models

diabetes_model=pickle.load(open('/Users/kishlaykumar/Documents/GitHub/Multiple_Disease_Prediction_System/Models/diabetes_model.sav','rb'))

heart_model=pickle.load(open('/Users/kishlaykumar/Documents/GitHub/Multiple_Disease_Prediction_System/Models/heart_model.sav','rb'))

parkinsons_model=pickle.load(open('/Users/kishlaykumar/Documents/GitHub/Multiple_Disease_Prediction_System/Models/parkinsons_model.sav','rb'))



#Sidebar for navigation

with st.sidebar:
    
    selected=option_menu("Multiple Disease Prediction System",
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         
                         icons=['droplet-half','heart-pulse-fill','person'],
                         
                          default_index=0)
    
     
    
# Diabetes Prediction page
if(selected=='Diabetes Prediction'):
    
    # Page Title
    st.title('Diabetes Prediction using ML')
    
    
    # Getting the input data from the user
    # Columns for Input fields
    col1, col2, col3= st.columns(3)
    
    with col1:
        Pregnancies =st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose =st.text_input('Glucose Level')
        
    with col3:
        BloodPressure =st.text_input('Blood Pressure Level')
        
    with col1:
        SkinThickness =st.text_input('Skin Thickness Level')
        
    with col2:
        Insulin =st.text_input('Insulin Level')
    
    with col3:
        BMI =st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age =st.text_input('Age of the Person') 

   
    
    
    
    # Code for Prediction
    
    diab_diagnosis=''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0] ==1):
            diab_diagnosis = 'The person is Diabetic.'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)  
    
    
    
    

    
# Heart Disease Prediction page
if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting ECG (0-2)')
        oldpeak = st.text_input('ST Depression')
        ca = st.text_input('Major Vessels (0-3)')

    with col2:
        sex = st.text_input('Sex (1=Male, 0=Female)')
        chol = st.text_input('Serum Cholesterol')
        thalach = st.text_input('Max Heart Rate')
        slope = st.text_input('Slope of ST segment')
        thal = st.text_input('Thalassemia (1=normal;2=fixed;3=reversible)')

    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
        fbs = st.text_input('Fasting Blood Sugar >120 mg/dl (1=True,0=False)')
        exang = st.text_input('Exercise Induced Angina (1=Yes,0=No)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            # Convert all inputs to float/int before prediction
            input_data = [float(age), int(sex), int(cp), float(trestbps), float(chol),
                          int(fbs), int(restecg), float(thalach), int(exang), float(oldpeak),
                          int(slope), int(ca), int(thal)]

            heart_prediction = heart_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is likely to have Heart Disease.'
            else:
                heart_diagnosis = 'The person is unlikely to have Heart Disease.'

        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values for all fields.'

    st.success(heart_diagnosis)






    
# Parkinson's Disease Prediction page
if selected == 'Parkinsons Prediction':

    st.title('Parkinsons Disease Prediction using ML')

    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        Jitter_DDP = st.text_input('Jitter:DDP')

    with col2:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        MDVP_APQ = st.text_input('MDVP:APQ')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        NHR = st.text_input('NHR')
        HNR = st.text_input('HNR')

    with col3:
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        try:
            # Convert all inputs to float
            input_data = [float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo), float(MDVP_Jitter),
                          float(MDVP_Jitter_Abs), float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                          float(MDVP_Shimmer), float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                          float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR),
                          float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]

            parkinsons_prediction = parkinsons_model.predict([input_data])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person is likely to have Parkinsons Disease.'
            else:
                parkinsons_diagnosis = 'The person is unlikely to have Parkinsons Disease.'

        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numeric values for all fields.'

    st.success(parkinsons_diagnosis)
