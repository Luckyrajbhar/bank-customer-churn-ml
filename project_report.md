# Bank Customer Churn Prediction Report

## 1. Project Overview
This project builds a machine learning solution to predict whether a bank customer will churn (leave the bank), based on customer demographics and transaction features.

## 2. Problem Statement
Customer churn leads to revenue loss for banks. The goal is to identify at-risk customers and support proactive retention strategies.

## 3. Data and Features
- Source dataset includes customer details such as credit score, age, tenure, balance, number of products, country, gender, and churn outcome.
- Irrelevant columns were removed.
- Encoded categorical variables using one-hot encoding for gender and country.
- Created a derived feature: `balance_per_product` = balance / (products_number + 1).

## 4. Preprocessing
- Standard scaling of numerical features using `StandardScaler`.
- One-hot encoding for categorical fields: gender and country.
- Feature engineering improved model interpretability and prediction performance.

## 5. Model Architecture
- Used an ensemble Voting Classifier combining:
  - Support Vector Machine (SVM)
  - Gradient Boosting Classifier
  - XGBoost Classifier
- Voting method: soft voting based on predicted probabilities.

## 6. Application and Deployment
- Interactive Streamlit app available via `app.py`.
- User inputs customer profile data and receives churn prediction probability.
- The app includes real-time prediction feedback and risk insight.

## 7. Files Added
- `Bank_Churn_Presentation.pptx`: Project presentation slides.
- `project_report.md`: Detailed project report.

## 8. Next Steps
- Add additional features and model tuning.
- Incorporate more customer behavior data.
- Convert the report to PDF if needed.
