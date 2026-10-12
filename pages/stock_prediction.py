import streamlit as st
import pandas as pd
import numpy as np
from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, fit_model, scale_data, get_forecast

st.set_page_config(page_title="Stock Prediction", layout="wide")
st.title("Stock Prediction")

ticker = st.text_input("Stock Ticker", value="AAPL")
st.subheader(f"Predicting Next 30 Days Close Price for {ticker}")

data = get_data(ticker)
close_price = data['Close']

rolling_price = get_rolling_mean(close_price)
d_order = get_differencing_order(rolling_price)
scaled_data, scaler = scale_data(rolling_price)

with st.spinner("Training model... Please wait (This might take a minute)."):
    # (p=30, d=calculated differencing, q=30)
    model, rmse = fit_model(scaled_data, order=(30, d_order, 30))
    st.success(f"Model RMSE Score: {round(rmse, 2)}")

forecast_scaled = get_forecast(model, steps=30)
forecast_actual = scaler.inverse_transform(np.array(forecast_scaled).reshape(-1, 1))

# Append the dates corresponding to the next 30 days
future_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=30)
forecast_df = pd.DataFrame(forecast_actual, index=future_dates, columns=['Forecasted Close'])

st.dataframe(forecast_df)

# Plot actual vs forecasted
combined_df = pd.DataFrame({
    'Actual Close': close_price.tail(150),
    'Forecasted Close': forecast_df['Forecasted Close']
})
st.line_chart(combined_df)
