🫀 Predicting Heart Disease Using Clinical and Genetic Features


📌 Overview
Heart disease is one of the leading causes of death worldwide. Traditional prediction methods rely on clinical indicators such as age, cholesterol levels, and blood pressure. However, genetic factors also play a significant role in cardiovascular risk.
This project explores whether incorporating genetic mutation features can improve the accuracy of heart disease prediction models.

🎯 Objective
The goal of this project is to:
Predict whether a patient has heart disease using machine learning
Compare model performance using:
Clinical features only
Clinical + genetic mutation features
Analyze whether genetic data improves prediction accuracy

📊 Dataset
We use the UCI Heart Disease Dataset, which contains patient health information.


🔹 Clinical Features
Age
Sex
Chest pain type (cp)
Resting blood pressure (trestbps)
Cholesterol (chol)
Fasting blood sugar (fbs)
Resting ECG (restecg)
Max heart rate (thalach)
Exercise-induced angina (exang)
ST depression (oldpeak)
Slope of ST segment (slope)
Number of vessels (ca)
Thalassemia (thal)


🔹 Target Variable
target:
1 = Heart Disease
0 = No Heart Disease


🧬 Genetic Features (Simulated)
To incorporate genetic influence, we added mutation-based features:
LDLR_mut → Cholesterol regulation
APOB_mut → Lipid transport
PCSK9_mut → Cholesterol metabolism
These features were synthetically generated to simulate real-world genetic risk factors and are more likely to appear in patients with heart disease.


🧪 Methodology
1. Data Preprocessing
Handled missing values
Encoded categorical variables
Split data into training and testing sets
2. Feature Engineering
Added simulated genetic mutation features
Created two datasets:
Clinical features only
Clinical + genetic features
3. Model Training
We trained the following models:
Logistic Regression
Random Forest
Each model was trained on:
Clinical data
Clinical + genetic data
4. Evaluation Metrics
Accuracy
F1 Score
Confusion Matrix
ROC Curve
