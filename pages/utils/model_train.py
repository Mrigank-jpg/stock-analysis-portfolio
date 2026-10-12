import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_data(ticker):
    return yf.download(ticker, start="2023-01-01")

def stationary_check(close_price):
    result = adfuller(close_price.dropna())
    return result[1] # Returning the p-value

def get_rolling_mean(close_price, window=7):
    # Applying rolling average to smooth out wild fluctuations
    return close_price.rolling(window=window).mean().dropna()

def get_differencing_order(close_price):
    d = 0
    p_value = stationary_check(close_price)
    while p_value > 0.05:
        d += 1
        close_price = close_price.diff().dropna()
        p_value = stationary_check(close_price)
    return d

def scale_data(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(np.array(data).reshape(-1, 1))
    return scaled_data, scaler

def fit_model(data, order):
    # 80/20 Train-Test Split for evaluation
    train_size = int(len(data) * 0.8)
    train, test = data[:train_size], data[train_size:]
    
    model = ARIMA(train, order=order)
    fitted_model = model.fit()
    predictions = fitted_model.forecast(steps=len(test))
    
    rmse = np.sqrt(mean_squared_error(test, predictions))
    # Note: Returning a model trained on the full dataset for future forecasting
    final_model = ARIMA(data, order=order).fit()
    return final_model, rmse

def get_forecast(model, steps=30):
    return model.forecast(steps=steps)
