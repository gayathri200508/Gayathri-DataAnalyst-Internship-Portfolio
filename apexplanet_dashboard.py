import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("ecommerce_data.csv")
    except:
        return pd.read_csv("1774067018886_ecommerce_data.csv")

df = load_data()

st.title("E-Commerce Dashboard")

with st.sidebar:
    st.header("Filters")
    categories = st.multiselect("Category", df["category"].unique(), default=df["category"].unique())
    regions = st.multiselect("Region", df["region"].unique(), default=df["region"].unique())
    payments = st.multiselect("Payment Method", df["payment_method"].unique(), default=df["payment_method"].unique())
    price = st.slider("Price Range", float(df["price"].min()), float(df["price"].max()), (float(df["price"].min()), float(df["price"].max())))

df = df[df["category"].isin(categories)]
df = df[df["region"].isin(regions)]
df = df[df["payment_method"].isin(payments)]
df = df[(df["price"] >= price[0]) & (df["price"] <= price[1])]

if df.empty:
    st.warning("No data")
    st.stop()

total_orders = len(df)
total_revenue = df["revenue"].sum()
avg_order = df["revenue"].mean()
total_qty = df["quantity"].sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Orders", total_orders)
c2.metric("Revenue", f"₹{int(total_revenue)}")
c3.metric("Avg Order", f"₹{int(avg_order)}")
c4.metric("Quantity", total_qty)

st.subheader("Revenue by Category")
cat_rev = df.groupby("category")["revenue"].sum().reset_index()
fig1 = px.bar(cat_rev, x="category", y="revenue")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Revenue Share")
fig2 = px.pie(cat_rev, values="revenue", names="category")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Price vs Revenue")
fig3 = px.scatter(df, x="price", y="revenue", color="category", size="quantity")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Category Analysis")
cat_stats = df.groupby("category").agg({
    "order_id":"count",
    "revenue":"sum",
    "price":"mean",
    "quantity":"sum"
}).reset_index()

st.dataframe(cat_stats)

st.subheader("Region Analysis")
region = df.groupby("region")["revenue"].sum().reset_index()
fig4 = px.bar(region, x="region", y="revenue")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Payment Analysis")
pay = df.groupby("payment_method")["revenue"].sum().reset_index()
fig5 = px.pie(pay, values="revenue", names="payment_method")
st.plotly_chart(fig5, use_container_width=True)

st.write("Done by Gayathri")
