# Bank Customer Churn Prediction Report

## 1. Project Overview
This AI-generated report describes a bank customer churn prediction solution that uses ensemble machine learning to identify customers at risk of leaving.

## 2. Problem Statement
Customer churn reduces revenue and increases acquisition cost. Predicting churn early enables banks to implement targeted retention strategies.

## 3. Data and Features
- Dataset includes credit score, age, tenure, balance, number of products, country, gender, and churn label.
- Removed irrelevant features such as customer ID.
- Encoded categorical variables: gender and country.
- Added `balance_per_product` as a new feature to capture customer engagement.

## 4. Preprocessing
- Standardized numerical features with `StandardScaler`.
- Applied one-hot encoding to categorical variables.
- Created a clean feature set for model training.

## 5. Model Architecture
- Trained an ensemble Voting Classifier.
- Combined SVM, Gradient Boosting, and XGBoost models.
- Used soft voting to aggregate prediction probabilities.

## 6. Application
- `app.py` is a Streamlit application for interactive churn prediction.
- Customers can be scored live based on input features.
- The app displays risk level and retention guidance.

## 7. Deliverables
- `Bank_Churn_Presentation.pptx`: AI-styled project presentation.
- `project_report.md`: Detailed written report.
- `generate_deliverables.py`: Script to regenerate deliverables anytime.

## 8. Recommendations
- Tune model hyperparameters and validate with cross-validation.
- Explore additional feature engineering and customer segmentation.
- Deploy the app for real-time retention analysis.
