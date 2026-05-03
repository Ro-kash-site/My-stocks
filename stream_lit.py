import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime


my_portfolio = {
    "HDFCBANK.BO": 10,       
    "SHRIRAMFIN.BO": 5,      
    "WIPRO.BO": 20,          
    "ANDHRAPET.BO": 50,      
    "JINDALSTEL.BO": 15
}

st.set_page_config(page_title="My Live Portfolio", page_icon="📈")

st.title("🚀 My Live Stock Tracker")
st.write(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

data = []
total_value = 0

with st.spinner('Updating prices...'):
    for ticker, shares in my_portfolio.items():
        try:
            stock = yf.Ticker(ticker)
         
            hist = stock.history(period="1d")
            if not hist.empty:
                price = hist['Close'].iloc[-1]
            else:
                price = 0
        except:
            price = 0
            
        current_value = price * shares
        total_value += current_value
        
        data.append({
            "Stock": ticker.replace(".NS", ""),
            "Price (₹)": round(price, 2),
            "Shares": shares,
            "Value (₹)": round(current_value, 2)
        })


df = pd.DataFrame(data)
st.table(df)


st.metric(label="Total Portfolio Value", value=f"₹{total_value:,.2f}")

if st.button("Refresh Now"):
    st.rerun()
