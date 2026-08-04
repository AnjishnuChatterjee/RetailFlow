import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Demand Forecast", layout="wide")

st.title("🔮 Demand Forecast")

forecast = pd.read_csv("data/processed/revenue_forecast.csv")

st.dataframe(forecast.head())

fig = px.line(
    forecast,
    x=forecast.columns[0],
    y=forecast.columns[1],
    title="Revenue Forecast"
)

st.plotly_chart(fig, use_container_width=True)