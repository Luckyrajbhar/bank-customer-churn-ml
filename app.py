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
        credit_score = st.slider("Credit Score", 300, 900, 600, key="credit_score")
        age = st.slider("Age", 18, 100, 30, key="age")

    with col2:
        tenure = st.slider("Tenure (Years)", 0, 10, 3, key="tenure")
        products_number = st.selectbox("Number of Products", [1, 2, 3, 4], key="products_number")

    with col3:
        country = st.selectbox("Country", ["France", "Germany", "Spain"], key="country")
        gender = st.selectbox("Gender", ["Female", "Male"], key="gender")

    col4, col5 = st.columns(2)
    with col4:
        active_member = st.selectbox("Active Member", ["Yes", "No"], key="active_member")
    with col5:
        balance_per_product = st.number_input(
            "Balance per Product", min_value=0.0, value=50000.0, format="%.2f", key="balance_per_product"
        )

# ------------------ Convert Inputs ------------------
active_member = 1 if active_member == "Yes" else 0
gender_Male = 1 if gender == "Male" else 0
country_Germany = 1 if country == "Germany" else 0
country_Spain = 1 if country == "Spain" else 0

st.markdown("---")

# ------------------ Prediction ------------------
if st.button("🚀 Predict Churn Risk", key="predict_button"):
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
