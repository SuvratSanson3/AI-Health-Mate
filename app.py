# Importing the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # This will load the local environment variables from the .env file

# Setup Gemini Api Key in vs code
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Streamlit App
st.header('🧑‍⚕️ AI :blue[Health Mate]⚕️',divider="red")
input = st.text_input('Hi! I am your Medical Expert 💊. Ask me anything...')
submit = st.button('Submit')

# Create a BMI Calculator - Sidebar
st.sidebar.header('BMI Calculator ✍️')
weight = st.sidebar.text_input('Enter your Weight (in kgs)') # Capture info in text
height = st.sidebar.text_input('Enter your Height (in cms)') 
# BMI = weight / (height/100)**2
height_num = pd.to_numeric(height)
weight_num = pd.to_numeric(weight)
bmi = weight_num / (height_num/100)**2
bmi = round(bmi,2)
st.sidebar.write(f'Your BMI is {bmi}')

# BMI Scale
notes = ''' The BMI is a convenient rule of thumb used to broadly categorize a person as 
underweight, normal weight, overweight, or obese based on tissue mass (muscle, fat, and bone) and height. 
Commonly accepted BMI ranges are: 
* underweight: under 18.5 kg/m2, 
* normal weight: 18.5 to 25, 
* overweight: 25 to 30, 
* obese: over 30. ''' 

if bmi < 18.5:
    st.sidebar.warning('Underweight')
    st.sidebar.write(notes)
elif bmi >= 18.5 and bmi < 25:
    st.sidebar.success('Normal Weight')
    st.sidebar.write(notes)    
elif bmi >= 25 and bmi < 30:
    st.sidebar.warning('Overweight')
    st.sidebar.write(notes)
else:
    st.sidebar.error('Obese')
    st.sidebar.write(notes)

# Generative AI Application

def get_response(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if text != "":
        response = model.generate_content(text)
        return (response.text)
    else:
        return "Please enter a valid input"

if submit:
    response = get_response(input)
    st.subheader(":green[The Response is :]")
    st.write(response)

# Disclaimer
st.subheader('Disclaimer: ',divider="red")
st.markdown('This application is for educational purposes only. Please consult a medical professional for any health-related concerns.')