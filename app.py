
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

