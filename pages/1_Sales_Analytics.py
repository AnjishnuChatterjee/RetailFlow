import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics", layout="wide")

st.title("📈 Sales Analytics")

df = pd.read_csv("data/processed/cleaned_retail.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


total_revenue = df["Revenue"].sum()
total_orders = df["Invoice"].nunique()
total_products = df["StockCode"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"${total_revenue:,.2f}")
col2.metric("Orders", total_orders)
col3.metric("Products", total_products)

monthly_sales = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Revenue"]
      .sum()
      .reset_index()
)

monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].astype(str)

fig = px.line(
    monthly_sales,
    x="InvoiceDate",
    y="Revenue",
    markers=True,
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)