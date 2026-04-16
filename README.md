# Bank Customer Churn Prediction

## Live Demo
🚀 **[View the Live App](https://your-app.streamlit.app)** (Replace with your actual Streamlit Cloud link after deployment)

## Overview
This project predicts whether a bank customer will churn (leave the bank) based on their profile and transaction data. It uses machine learning models to analyze customer behavior and provides an interactive web app for predictions.

## Problem Statement
Banks face significant revenue loss due to customer churn. Identifying customers likely to leave allows proactive retention strategies. The challenge is to build an accurate predictive model using customer data like age, balance, gender, country, and product usage.

## Solution Approach
1. **Data Exploration**: Analyzed the dataset for distributions, correlations, and patterns using EDA (Exploratory Data Analysis).
2. **Preprocessing**:
   - Dropped irrelevant columns (e.g., customer_id).
   - Encoded categorical variables (gender, country) using one-hot encoding.
   - Created new features (e.g., balance_per_product = balance / (products_number + 1)).
   - Scaled numerical features for model training.
3. **Model Training**: Used a Voting Classifier combining SVM, Gradient Boosting Classifier, and XGBoost for robust predictions.
4. **Web App**: Built an interactive Streamlit app for real-time predictions.

## Features
- Predict churn probability based on user inputs.
- Visual EDA insights in the Jupyter notebook.
- Trained model with high accuracy using ensemble methods.

## Files Description
- `app.py`: Streamlit web app for predictions.
- `train.py`: Script for data preprocessing and model training.
- `Bank churn analysis.ipynb`: Jupyter notebook with EDA and visualizations.
- `model.pkl`: Trained Voting Classifier model.
- `scaler.pkl`: StandardScaler for feature scaling.
- `requirements.txt`: Python dependencies.
- `vercel.json`: Configuration for deployment (though not used due to compatibility).

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Luckyrajbhar/bank-customer-churn-ml.git
   cd bank-customer-churn-ml
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- **Run Locally**:
  ```
  streamlit run app.py
  ```
  Open the link in your browser.

- **Deployed App**: Available on Render/Streamlit Cloud (link provided after deployment).

## How the Problem Was Handled
- **Data Handling**: Cleaned data, handled categorical encoding, and feature engineering to improve model performance.
- **Model Selection**: Chose ensemble methods for better accuracy and generalization.
- **Deployment**: Made the model accessible via a user-friendly web interface.
- **Challenges**: Ensured compatibility with deployment platforms; switched from Vercel to Render due to Streamlit requirements.

## Technologies Used
- Python, Pandas, Scikit-learn, XGBoost
- Streamlit for the web app
- Matplotlib, Seaborn for visualizations
- Git for version control

## Future Improvements
- Add more features or models.
- Integrate real-time data.
- Improve UI/UX.

## License
MIT License