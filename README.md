Heart Disease Prediction using Machine Learning
📌 Project Overview

This project predicts the presence of heart disease in patients using machine learning techniques. It analyzes medical attributes to support early diagnosis and improve healthcare decision-making.

📊 Dataset

The dataset consists of patient health information including:

Age, Sex
Chest Pain Type
Resting Blood Pressure
Serum Cholesterol
Fasting Blood Sugar
Resting ECG Results
Maximum Heart Rate Achieved
Exercise-Induced Angina
Number of Major Vessels
Thalassemia

Target Variable:
heart_disease_present (0 = No, 1 = Yes)

⚙️ Technologies Used
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn

🔍 Data Preprocessing
Merged datasets using patient ID
Removed unnecessary columns
Encoded categorical features
Handled outliers using Winsorization
Applied feature scaling

📈 Exploratory Data Analysis
Correlation heatmap
Distribution plots
Feature relationship analysis

🤖 Models Implemented
Logistic Regression
Decision Tree
Gradient Boosting

🎯 Model Evaluation

Performance evaluated using:
Accuracy
Precision
Recall
F1-Score
Confusion Matrix

📊 Results
Model	Accuracy
Logistic Regression	83%
Decision Tree	83%
Gradient Boosting	~80%

🏆 Best Model
Logistic Regression and Decision Tree achieved the best performance with ~83% accuracy.

📌 Key Insights
Age and maximum heart rate are key predictors
Cholesterol and chest pain significantly impact results
Exercise-induced angina strongly correlates with heart disease

💾 Model Saving
import joblib
joblib.dump(model, "heart_disease_model.pkl")

🚀 Future Improvements
Use advanced models (Random Forest, XGBoost)
Improve hyperparameter tuning
Deploy using Streamlit
Use larger datasets

📁 Project Structure
├── data/
├── notebook.ipynb
├── README.md
├── heart_disease_model.pkl

🙌 Conclusion
This project demonstrates how machine learning can effectively predict heart disease and assist in healthcare analytics.
