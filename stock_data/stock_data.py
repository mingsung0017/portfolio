import yfinance as yf
import streamlit as st

st.write("""
# Stock History Web App
### Displaying chosen stock's closing price and volume 
### YTD with 1 Day interval
""")

#define the default ticker symbol as Apple Inc. 'AAPL'
ticker = 'AAPL'

#sidebar area to get user's input for ticker symbol
st.sidebar.header('User Input Stock Ticker')
ticker = st.sidebar.text_input('Ticker', 'AAPL')


#get data on this ticker
tickerData = yf.Ticker(ticker)
#get the historical data for this ticker
tickerDf = tickerData.history(period='ytd', interval='1d')


st.write('Ticker: ' + ticker)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)