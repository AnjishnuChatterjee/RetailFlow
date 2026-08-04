import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Inventory Analysis", layout="wide")

st.title("📦 Inventory Analysis")

inventory = pd.read_csv("data/processed/inventory_analysis.csv")

st.dataframe(inventory.head())

top = inventory.sort_values(
    "TotalRevenue",
    ascending=False
).head(10)

fig = px.bar(
    top,
    x="Description",
    y="TotalRevenue",
    title="Top Revenue Products"
)

st.plotly_chart(fig, use_container_width=True)