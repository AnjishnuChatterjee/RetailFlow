import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn", layout="wide")

st.title("⚠️ Customer Churn Prediction")

churn = pd.read_csv("data/processed/customer_churn.csv")

st.dataframe(churn.head())

st.metric(
    "Customers Likely to Churn",
    int(churn["Churn"].sum())
)