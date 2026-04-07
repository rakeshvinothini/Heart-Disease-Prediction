import numpy as np
import joblib

# Load trained model

model = joblib.load("heart_disease_model.pkl")

def predict_heart_disease(data):
prediction = model.predict([data])
return prediction[0]

if **name** == "**main**":
print("❤️ Heart Disease Prediction System")
print("----------------------------------")

```
slope = int(input("Slope of peak exercise ST segment (1-3): "))
thal = int(input("Thal (encoded value): "))
resting_bp = int(input("Resting Blood Pressure: "))
chest_pain = int(input("Chest Pain Type (1-4): "))
vessels = int(input("Number of Major Vessels (0-3): "))
fasting_bs = int(input("Fasting Blood Sugar > 120 (0/1): "))
ekg = int(input("Resting ECG Results (0-2): "))
cholesterol = int(input("Serum Cholesterol: "))
oldpeak = float(input("Oldpeak (ST depression): "))
sex = int(input("Sex (0 = Female, 1 = Male): "))
age = int(input("Age: "))
max_hr = int(input("Max Heart Rate Achieved: "))
angina = int(input("Exercise Induced Angina (0/1): "))

user_data = [
    slope, thal, resting_bp, chest_pain, vessels,
    fasting_bs, ekg, cholesterol, oldpeak,
    sex, age, max_hr, angina
]

result = predict_heart_disease(user_data)

print("\n🔍 Prediction Result:")
if result == 1:
    print("⚠️ Heart Disease Detected")
else:
    print("✅ No Heart Disease")
```
