import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("👥 Customer Segmentation")

segments = pd.read_csv("data/processed/customer_segments.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Customers", len(segments))

with col2:
    st.metric("Number of Segments", segments["Cluster"].nunique())


st.subheader("Customer Segments Data")
st.dataframe(segments.head())

fig = px.scatter(
    segments,
    x="Frequency",
    y="Monetary",
    color="Cluster",
    title="Customer Segments"
)

st.plotly_chart(fig, use_container_width=True)