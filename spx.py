import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime


st.write("""
# Simple Stock Price App
""")

st.sidebar.header("Enter symbol")


tickerSymbol = 'SPY'
symbol = st.sidebar.text_area("", tickerSymbol)

st.sidebar.header('Enter dates')

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
ayearago = yesterday - datetime.timedelta(days=365)
start_date = st.sidebar.date_input('Start date', ayearago)
end_date = st.sidebar.date_input('End date', yesterday)


st.write("""### Current symbol:
	""", symbol)


tickerData = yf.Ticker(symbol)
tickerDf = tickerData.history(period='1d', start=str(start_date), end=str(end_date))

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

tickerDf['% change'] = (tickerDf.Close - tickerDf.Open) / tickerDf.Open * 100
fig = sns.displot(tickerDF['% change'], bins=50, kde=True)
#fig = plt.hist(tickerDf['% change'], bins=50)

#arr = np.random.normal(1, 1, size=100)
#fig, ax = plt.subplots()
#ax.hist(arr, bins=20)
st.pyplot(fig)
#st.bar_chart(tickerDf['% change'])

def filedownload(df):
	csv = df.to_csv()
	href = f'<a href="data:file/csv;{csv}"  download="summary.csv"> Download CSV File</a>'
	return href

ticker_described = tickerDf.describe()
ticker_described.reset_index(level=0, inplace=True)

ticker_described.columns = ['feature']+list(ticker_described.columns)[1:]


st.write(ticker_described)
st.markdown(filedownload(ticker_described), unsafe_allow_html=True)
