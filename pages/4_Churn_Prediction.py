import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn", layout="wide")

st.title("⚠️ Customer Churn Prediction")


churn = pd.read_csv("data/processed/customer_churn.csv")

total_customers = len(churn)
churned = churn["Churn"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "Likely to Churn",
        churned
    )

st.subheader("Customer Churn Data")

st.dataframe(churn.head())
