import streamlit as st
import numpy as np
import joblib

# Load model

model = joblib.load("heart_disease_model.pkl")

st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details below:")

# Input fields

slope = st.selectbox("Slope of peak exercise ST segment", [1, 2, 3])
thal = st.number_input("Thal (encoded value)", min_value=0)
resting_bp = st.number_input("Resting Blood Pressure")
chest_pain = st.selectbox("Chest Pain Type", [1, 2, 3, 4])
vessels = st.selectbox("Number of Major Vessels", [0, 1, 2, 3])
fasting_bs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
ekg = st.selectbox("Resting ECG Results", [0, 1, 2])
cholesterol = st.number_input("Serum Cholesterol")
oldpeak = st.number_input("Oldpeak (ST depression)")
sex = st.selectbox("Sex", [0, 1])
age = st.number_input("Age")
max_hr = st.number_input("Max Heart Rate Achieved")
angina = st.selectbox("Exercise Induced Angina", [0, 1])

# Prediction button

if st.button("Predict"):
user_data = np.array([
slope, thal, resting_bp, chest_pain, vessels,
fasting_bs, ekg, cholesterol, oldpeak,
sex, age, max_hr, angina
]).reshape(1, -1)

```
result = model.predict(user_data)

if result[0] == 1:
    st.error("⚠️ Heart Disease Detected")
else:
    st.success("✅ No Heart Disease")
```
