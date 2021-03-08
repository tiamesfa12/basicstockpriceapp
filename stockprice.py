import yfinance as yf 
import streamlit as st 
import pandas as pd 

st.write("""
# Basic stock price app

showing the stock of Tesla at its closing price and the volume.



""")


#define the ticker symbol 
tickerSymbol = 'TSLA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the history prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2020-5-31')
# open high, low close, volume, dividends, stock splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)