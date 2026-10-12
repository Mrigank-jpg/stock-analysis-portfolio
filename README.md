
End-to-End Stock Analysis & Prediction App

Welcome to my Stock Analysis Portfolio Project! This is a web-based application built entirely in Python. It allows users to look up any stock, view real-time financial data, and use machine learning (Time Series Forecasting) to predict how the stock's price might move over the next 30 days.

I built this project to showcase my skills in Data Analysis, API Integration, and Machine Learning using a friendly user interface.

What Does This App Do?

This app is divided into different pages, each serving a specific purpose:

Home Page: A clean landing page that introduces the app and the services it provides.

Stock Analysis:

You can type in any stock ticker (like AAPL for Apple or TSLA for Tesla) and pick a date range.

The app reaches out to Yahoo Finance in real-time to grab company details, Market Cap, P/E ratios, and live pricing.

It displays the daily price changes and interactive charts of the historical data.

Stock Prediction:

This is where the machine learning happens!

The app takes the historical closing prices of a stock and trains an ARIMA (AutoRegressive Integrated Moving Average) statistical model in the background.

It calculates the math needed to make the data "stationary" (easy for the model to read) and predicts the closing prices for the next 30 days, plotting them on a beautiful chart.

How the Code is Organized

If you are looking through my code, here is a simple guide to what each file does:

portfolio_project/
├── trading_app.py                <-- The main entry point for the Streamlit web app.
├── requirements.txt              <-- A list of all the Python libraries needed to run the app.
├── .gitignore                    <-- Tells Git which private/system files to ignore.
└── pages/
    ├── stock_analysis.py         <-- The code for the Stock Analysis page and charts.
    ├── stock_prediction.py       <-- The code for the Prediction page and ARIMA forecasting.
    └── utils/
        ├── model_train.py        <-- The heavy lifting! Contains the math, scaling, and ARIMA model logic.
        └── plotly_figure.py      <-- A helper file that makes the data tables look pretty using Plotly.


Technology Stack (Tools I Used)

Streamlit: To build the web application interface without needing HTML/CSS.

yFinance: To pull live, real-world stock market data from Yahoo.

Pandas: To clean, organize, and structure the data into tables (DataFrames).

Plotly: To draw the interactive charts and graphs.

Statsmodels (ARIMA): The core statistical library used to forecast future stock prices.

Scikit-Learn: Used for scaling the data and calculating the error score (RMSE) of the predictions.

How to Run This Project on Your Own Computer

If you want to download and run this app locally, follow these simple steps:

1. Clone the repository:

git clone https://github.com/YourUsername/stock-analysis-portfolio.git
cd stock-analysis-portfolio


(Make sure to replace YourUsername with your actual GitHub username!)

2. Create a virtual environment:
This keeps the project's dependencies separate from your computer's main Python installation.

python -m venv stockenv


3. Activate the environment:

Windows (PowerShell): .\stockenv\Scripts\Activate.ps1

Mac/Linux: source stockenv/bin/activate

4. Install the required libraries:

pip install -r requirements.txt


5. Start the app!

streamlit run trading_app.py


A browser window will automatically pop up showing the app in action!

Recent Problem Solving

Data Structure Update: Recently, the yfinance API changed how it delivers data, switching to a "Multi-Index" format which crashed standard data apps. I successfully debugged this by adding custom logic to flatten the data structure back into a standard 1D format before feeding it into the app and the predictive model.