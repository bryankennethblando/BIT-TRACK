import streamlit as st
import pandas as pd

st.title("Crypto Price Tracker MVP")
st.write("Tracking the top 10 highest-priced cryptocurrencies.")

df = pd.read_csv("data/crypto_data.csv")

st.write("### Raw Data")
st.dataframe(df)

st.write("### Price Comparison")
chart_data = df.set_index('symbol')['price']
st.bar_chart(chart_data)