import streamlit as st
import pandas as pd

from src.api_fecher import update_data

st.set_page_config(page_title="Crypto Tracker", page_icon="📈", layout="wide")

st.title("Crypto Price Tracker MVP")
st.write("Tracking the top 5 highest-priced cryptocurrencies.")

if st.button("Fetch Live Prices 🔄"):
    with st.spinner("Fetching data from Binance"):
        success = update_data()

        if success:
            st.success("Data updated successfully!")
        else:
            st.error("Failed to update data.")

try:
    df = pd.read_csv("data/crypto_data.csv")

    # --- NEW: Dashboard KPI Metrics ---
    st.write("### 🏆 Top 5 Market Leaders")
    # Create 3 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Display the top 3 coins in the columns using st.metric
    with col1:
        st.metric(label=df.iloc[0]['symbol'], value=f"${df.iloc[0]['price']:,.2f}")
    with col2:
        st.metric(label=df.iloc[1]['symbol'], value=f"${df.iloc[1]['price']:,.2f}")
    with col3:
        st.metric(label=df.iloc[2]['symbol'], value=f"${df.iloc[2]['price']:,.2f}")
    with col4:
        st.metric(label=df.iloc[3]['symbol'], value=f"${df.iloc[3]['price']:,.2f}")
    with col5:
        st.metric(label=df.iloc[4]['symbol'], value=f"${df.iloc[4]['price']:,.2f}")
    
    st.markdown("---") # Visual divider
    # ----------------------------------

    st.write("### Price Comparison")
    chart_data = df.set_index('symbol')['price']
    st.bar_chart(chart_data)

    st.write("### Raw Data Table")
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.warning("No data found. Please click the  'Fetch Live Prices' button above.")