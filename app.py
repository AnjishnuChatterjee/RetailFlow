import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="RetailFlow Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed/cleaned_retail.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.header("Dashboard Filters")

# Country Filter
countries = sorted(df["Country"].dropna().unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + countries
)

# Date Filter
start_date = st.sidebar.date_input(
    "Start Date",
    df["InvoiceDate"].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["InvoiceDate"].max().date()
)

filtered_df = df.copy()

# Country Filter
if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

# Date Filter
filtered_df = filtered_df[
    (filtered_df["InvoiceDate"].dt.date >= start_date) &
    (filtered_df["InvoiceDate"].dt.date <= end_date)
]

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("📊 RetailFlow Dashboard")

st.markdown("""
Welcome to the **RetailFlow AI-Powered Customer Analytics & Demand Forecasting Platform**.

Use the navigation menu on the left to explore:

- 📈 Sales Analytics
- 👥 Customer Segmentation
- 🔮 Demand Forecasting
- ⚠️ Churn Prediction
- 📦 Inventory Analysis
""")

# -----------------------------
# Calculate KPIs
# -----------------------------
total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["Invoice"].nunique()
total_customers = df["Customer ID"].nunique()
average_order = total_revenue / total_orders

# -----------------------------
# Display KPIs
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Revenue", f"${total_revenue:,.2f}")

with col2:
    st.metric("Orders", total_orders)

with col3:
    st.metric("Customers", total_customers)

with col4:
    st.metric("Average Order Value", f"${average_order:,.2f}")

# -----------------------------
# Dataset Preview
# -----------------------------

st.divider()
st.sidebar.title("RetailFlow")

st.sidebar.success("Navigation")

st.sidebar.write("""
Welcome to RetailFlow Dashboard.
Use the sidebar to navigate through analytics.
""")
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(10))

st.download_button(
    label="📥 Download Sales Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.divider()

st.subheader("📈 Monthly Revenue Trend")

monthly_sales = (
    filtered_df.groupby(filtered_df["InvoiceDate"].dt.to_period("M"))["Revenue"]
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

st.subheader("🌍 Revenue by Country")

country_sales = (
    filtered_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    country_sales,
    x="Country",
    y="Revenue",
    color="Revenue",
    title="Top 10 Countries by Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🏆 Top Selling Products")

top_products = (
    filtered_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    color="Revenue",
    title="Top 10 Products"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("👥 Top Customers")

top_customers = (
    filtered_df.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_customers,
    x="Customer ID",
    y="Revenue",
    color="Revenue",
    title="Top Customers"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Current Filters")

st.write(f"Country: **{selected_country}**")

st.write(f"Date Range: **{start_date} → {end_date}**")

st.divider()

st.header("About RetailFlow")

st.write("""
RetailFlow is an AI-powered analytics platform that helps retailers:

- Analyze customer purchasing behavior
- Forecast future demand
- Predict customer churn
- Optimize inventory
- Visualize business performance

Built using:
- Python
- Pandas
- Scikit-learn
- Prophet
- Streamlit
""")