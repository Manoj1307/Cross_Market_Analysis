import streamlit as st
from streamlit_option_menu import option_menu
import market_overview as mo
import querry_runner as qr
import top_crypto_analysis as ta
import pandas as pd

st.set_page_config(layout='wide')

with st.sidebar:
    select = option_menu('Cross Market Analysis Dashboard', ['Market-Overview', 'Query Runner', 'Crypto Analysis'])

def market_overview():
    st.header('Market Overview')
    st.write('This section provides an overview of the market trends and key Indicators.')
    col1, col2, col3, col4= st.columns(4)
    data = mo.get_avg_price()
    col1.metric("Avg Bitcoin Price", f"{data['BITCOIN']:.2f}")
    col2.metric("Avg Oil Price", f"{data['OIL']:.2f}")
    col3.metric("Avg S&P 500", f"{data['S&P 500']:.2f}")
    col4.metric("Avg Nifty", f"{data['NIFTY']:.2f}")
    col01, col0 = st.columns(2)
    data = mo.get_market_comparison()

    df = pd.DataFrame(data, columns=["DATE", "STOCK_PRICE", "OIL_PRICE", "BTC_PRICE"])

    st.dataframe(df)

def query_runner():
    st.title("🔍 Query Runner")
    query_name = st.selectbox(
        "Select Query",
        list(qr.querries.keys())
    )
    sql = qr.querries[query_name]
    #st.code(sql, language="sql")
    if st.button("Run Query"):
        df = qr.run_query(sql)
        st.dataframe(df)

def crypto_analysis():
    st.title("Top Crypto Analysis")
    st.write("This section provides analysis of top cryptocurrencies based on market capitalization and other key metrics.")
    ids = ta.getids()
    selected_id = st.selectbox("", options= ids, index = 0)
    col6, col7 = st.columns(2)
    with col6:
        sdate = st.date_input("Start Date")
    with col7:
        edate = st.date_input("End Date")
    df = ta.price_chart(selected_id, sdate, edate)
    st.line_chart(df.set_index("DATE")["PRICE_INR"])

    df_daily = ta.daily_price(selected_id)
    st.write("Daily Prices for Selected Cryptocurrency:")
    st.dataframe(df_daily)

if select == "Market-Overview":
    market_overview()

elif select == "Query Runner":
    query_runner()

elif select == "Crypto Analysis":
    crypto_analysis()