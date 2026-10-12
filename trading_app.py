import streamlit as st

# Configure the Streamlit page
st.set_page_config(page_title="Trading App", layout="wide", page_icon="heavy_dollar_sign")
st.title("Trading Guide App")
st.subheader("We provide the greatest platform for you to collect all information prior to investing in stock")

st.markdown("""
### We provide the following services:
1️⃣ **Stock Information** - Real-time stock data and descriptive statistics.
2️⃣ **Stock Prediction** - Forecasting the next 30 days of closing prices using Time Series Analysis.
3️⃣ **CAPM Return** - Compare expected returns against market risk.
4️⃣ **CAPM Beta** - Evaluate stock volatility and systemic risk.
""")
