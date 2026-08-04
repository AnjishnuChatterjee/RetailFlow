import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Inventory Analysis", layout="wide")

st.title("📦 Inventory Analysis")


inventory = pd.read_csv("data/processed/inventory_analysis.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Products",
        len(inventory)
    )

with col2:
    st.metric(
        "High Demand Products",
        len(
            inventory[
                inventory["InventoryStatus"] == "High Demand"
            ]
        )
    )


st.subheader("Inventory Data")

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