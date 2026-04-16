import streamlit as st
import pickle
import numpy as np
import os
import time

# ------------------ Load Model ------------------
base_dir = os.path.dirname(__file__)
model = pickle.load(open(os.path.join(base_dir, "model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(base_dir, "scaler.pkl"), "rb"))

# ------------------ Page Config ------------------
st.set_page_config(page_title="Bank Customer Churn Predictor", page_icon="🏦", layout="wide")

st.markdown(
    "<style>"
    "body {background-color: #f1f5f9;}"
    ".stApp {background-color: #f1f5f9;}"
    ".stButton>button {background-color: #0b4f6c; color: white; border-radius: 12px; height: 3em; width: 100%;}"
    ".css-1d391kg {background-color: #ffffff; border-radius: 18px; padding: 1.5rem;}"
    "</style>",
    unsafe_allow_html=True,
)

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("🏦 Bank Churn Predictor")
    st.write("Estimate customer churn risk using an AI-powered model and take action before it's too late.")
    st.divider()
    st.subheader("How to use")
    st.write("• Enter customer profile details.")
    st.write("• Click Predict to compute churn probability.")
    st.write("• Review recommendations for retention.")
    st.divider()
    st.subheader("Model details")
    st.write("Ensemble classifier with SVM, Gradient Boosting, and XGBoost.")
    st.write("Input features are scaled for consistent predictions.")

# ------------------ Header ------------------
st.title("Bank Customer Churn Prediction")
st.markdown("#### Predict churn risk and prioritize customer retention with confidence.")

# ------------------ Input Section ------------------
with st.container():
    st.markdown("---")
    st.subheader("Customer Details")
    col1, col2, col3 = st.columns(3)

    with col1:
        credit_score = st.slider("Credit Score", 300, 900, 600)
        age = st.slider("Age", 18, 100, 30)

    with col2:
        tenure = st.slider("Tenure (Years)", 0, 10, 3)
        products_number = st.selectbox("Number of Products", [1, 2, 3, 4])

    with col3:
        country = st.selectbox("Country", ["France", "Germany", "Spain"])
        gender = st.selectbox("Gender", ["Female", "Male"])

    col4, col5 = st.columns(2)
    with col4:
        active_member = st.selectbox("Active Member", ["Yes", "No"])
    with col5:
        balance_per_product = st.number_input(
            "Balance per Product", min_value=0.0, value=50000.0, format="%.2f"
        )

# ------------------ Convert Inputs ------------------
active_member = 1 if active_member == "Yes" else 0
gender_Male = 1 if gender == "Male" else 0
country_Germany = 1 if country == "Germany" else 0
country_Spain = 1 if country == "Spain" else 0

st.markdown("---")

# ------------------ Prediction ------------------
if st.button("🚀 Predict Churn Risk"):
    data = np.array(
        [[
            credit_score,
            age,
            tenure,
            products_number,
            active_member,
            gender_Male,
            country_Germany,
            country_Spain,
            balance_per_product,
        ]]
    )

    data = scaler.transform(data)

    with st.spinner("Analyzing risk profile..."):
        time.sleep(1)

    prediction = model.predict(data)
    prob = model.predict_proba(data)[0][1]
    churn_pct = prob * 100
    stay_pct = 100 - churn_pct

    st.subheader("Prediction Summary")
    col6, col7 = st.columns(2)
    with col6:
        st.metric(label="Churn Probability", value=f"{churn_pct:.2f}%")
    with col7:
        st.metric(label="Stay Probability", value=f"{stay_pct:.2f}%")

    if prediction[0] == 1:
        st.error(f"❌ High churn risk: {churn_pct:.2f}%")
    else:
        st.success(f"✅ Low churn risk: {churn_pct:.2f}%")

    st.markdown("### Recommended Action")
    if prob > 0.75:
        st.warning("Immediate retention action recommended for this customer.")
    elif prob > 0.4:
        st.info("Monitor this customer and consider targeted offers.")
    else:
        st.success("Customer is stable. Continue normal engagement.")

st.markdown("---")
st.caption("Built with Streamlit | Bank Customer Churn Prediction")

import streamlit as st
import pickle
import numpy as np
import os
import time

# ------------------ Load Model ------------------
base_dir = os.path.dirname(__file__)
model = pickle.load(open(os.path.join(base_dir, "model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(base_dir, "scaler.pkl"), "rb"))

# ------------------ Page Config ------------------
st.set_page_config(page_title="Bank Churn Predictor", layout="centered")

# ------------------ Title ------------------
st.title("🏦 Bank Customer Churn Prediction")
st.markdown("### Predict whether a customer will leave the bank")
st.markdown("---")

# ------------------ Input Section ------------------
st.subheader("📋 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    credit_score = st.slider("Credit Score", 300, 900, 600)
    age = st.slider("Age", 18, 100, 30)
    tenure = st.slider("Tenure (Years)", 0, 10, 3)

with col2:
    products_number = st.selectbox("Number of Products", [1, 2, 3, 4])
    active_member = st.selectbox("Active Member", ["No", "Yes"])
    gender = st.selectbox("Gender", ["Female", "Male"])

st.subheader("🌍 Location & Balance")

col3, col4 = st.columns(2)

with col3:
    country = st.selectbox("Country", ["France", "Germany", "Spain"])

with col4:
    balance_per_product = st.number_input("Balance per Product", value=50000.0)

# ------------------ Convert Inputs ------------------
active_member = 1 if active_member == "Yes" else 0
gender_Male = 1 if gender == "Male" else 0
country_Germany = 1 if country == "Germany" else 0
country_Spain = 1 if country == "Spain" else 0




# ------------------ Prediction ------------------
st.markdown("---")

if st.button("🚀 Predict"):

    data = np.array([[credit_score, age, tenure, products_number,
                      active_member, gender_Male,
                      country_Germany, country_Spain,
                      balance_per_product]])

    data = scaler.transform(data)

    with st.spinner("🔍 Analyzing data..."):
        time.sleep(1)

    prediction = model.predict(data)
    prob = model.predict_proba(data)[0][1]

    st.subheader("📊 Prediction Result")

    # Progress bar
    st.progress(int(prob * 100))

    if prediction[0] == 1:
        st.error(f"❌ Customer will churn ({prob*100:.2f}%)")
    else:
        st.success(f"✅ Customer will stay ({prob*100:.2f}%)")

    # Insight
    st.markdown("### 💡 Insight")

    if prob > 0.7:
        st.warning("High risk customer. Take action!")
    elif prob > 0.4:
        st.info("Moderate risk. Monitor behavior.")
    else:
        st.success("Low risk. Customer is stable.")

# ------------------ Footer ------------------
st.markdown("---")
st.caption("💡 Built with Streamlit | Data Science Project")

