import yfinance as yf
import streamlit as st
from datetime import date

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Apple!

""")

st.sidebar.header('Data settings')
StartDay = st.sidebar.date_input('Start day',value=date(2000,1,1), min_value=date(2000,1,1), max_value=date.today())
EndDay = st.sidebar.date_input('End day', min_value=StartDay, max_value=date.today())

StartDayStr = StartDay.strftime('%Y-%m-%d')
EndDayStr = EndDay.strftime('%Y-%m-%d')

#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=StartDayStr, end=EndDay)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
