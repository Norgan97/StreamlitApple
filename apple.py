import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Приложение для отслеживания акций

**Показаны данные для компании Apple**

""")
         
#Определяем тикер нужной компании
tickerSymbol = 'AAPL'
#Получаем данные из тикера
tickerData = yf.Ticker(tickerSymbol)
#Получаем историю цен для этого тикера по указанному периоду
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write("""
## Цена закрытия
""")
st.line_chart(tickerDf.Close)

st.write("""
## Объём
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Цена открытия
""")
st.line_chart(tickerDf.Open)

st.write("""
## Пиковая цена за день
""")
st.line_chart(tickerDf.High)

st.write("""
## Диведенды
""")
st.line_chart(tickerDf.Dividends)

st.write("""
## Самая низкая цена за день
""")
st.line_chart(tickerDf.Low)
