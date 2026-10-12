import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from pages.utils.plotly_figure import plotly_table

st.set_page_config(page_title="Stock Analysis", page_icon="📈", layout="wide")
st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)
today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", value="TSLA")
with col2:
    start_date = st.date_input("Choose Start Date", value=datetime.date(today.year - 1, today.month, today.day))
with col3:
    end_date = st.date_input("Choose End Date", value=today)

st.subheader(ticker)
stock = yf.Ticker(ticker)

st.write("**Sector:** ", stock.info.get('sector'))
st.write("**Full Time Employees:** ", stock.info.get('fullTimeEmployees'))
st.write("**Website:** ", stock.info.get('website'))

# Generate Custom Dataframe for specific Metrics
df_info = pd.DataFrame(index=['Market Cap', 'Beta', 'Trailing EPS', 'Trailing PE'])
df_info['Value'] = [
    stock.info.get('marketCap'), 
    stock.info.get('beta'), 
    stock.info.get('trailingEps'), 
    stock.info.get('trailingPE')
]
st.plotly_chart(plotly_table(df_info.reset_index()), use_container_width=True)

# Historical Data
data = yf.download(ticker, start=start_date, end=end_date)
if not data.empty and len(data) > 1:
    daily_change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
    st.metric(label="Daily Change", value=round(data['Close'].iloc[-1], 2), delta=round(daily_change, 2))

st.subheader("Historical Data (Last 10 Days)")
last_10_df = data.sort_index(ascending=False).head(10).round(2)
st.plotly_chart(plotly_table(last_10_df.reset_index()), use_container_width=True)

st.line_chart(data['Close'])
