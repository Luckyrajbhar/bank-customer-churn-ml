import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
import xgboost as xgb

# Load data
df = pd.read_csv("C:\Users\lucky\Documents\Lucky\Bank_Customer_Churn_prediction\Bank Customer Churn Prediction.csv")

# Drop unnecessary columns
df = df.drop(columns=["customer_id"])

# Encoding
df = pd.get_dummies(df, columns=['gender', 'country'], drop_first=True)

# Feature engineering
df['balance_per_product'] = df['balance'] / (df['products_number'] + 1)

# Drop unwanted columns
df = df.drop(['balance', 'estimated_salary', 'credit_card'], axis=1)

# Split
X = df.drop("churn", axis=1)
y = df["churn"]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Models
svm = SVC(probability=True)
gbc = GradientBoostingClassifier()
xgb_model = xgb.XGBClassifier(random_state=42, verbosity=0)

# Voting model (your final model)
voting_model = VotingClassifier(
    estimators=[
        ('svm', svm),
        ('gbc', gbc),
        ('xgb', xgb_model)
    ],
    voting='soft'
)

# Train
voting_model.fit(X_train, y_train)





print("Model and scaler saved successfully!")