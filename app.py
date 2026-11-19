import streamlit as st
import pandas as pd

df = pd.read_csv("cafe_sales.csv")

st.title("Qahwa Corner Sales Dashboard")

branch = st.selectbox("Select branch", sorted(df["branch"].unique()))
data = df[df["branch"] == branch]

st.metric("Total revenue (SAR)", int(data["total_sar"].sum()))
st.bar_chart(data.groupby("product")["total_sar"].sum())
