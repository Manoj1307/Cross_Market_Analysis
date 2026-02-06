import streamlit as st
from streamlit_option_menu import option_menu
import market_overview as mo
import querry_runner as qr
import top_crypto_analysis as ta

st.set_page_config(layout='wide')

with st.sidebar:
    select = option_menu('Cross Market Analysis Dashboard', ['Market-Overview', 'Query Runner', 'Crypto Analysis'])

def market_overview():
    st.header('Market Overview')
    st.write('This section provides an overview of the market trends and key Indicators.')
    ids = mo.getids()
    selected_id = st.selectbox("", options= ids, index = 0)
    price = mo.get_price(selected_id)
    if price is not None:
        st.metric("Current Price", f"₹{price:,.2f}")
    else:
        st.warning("No data found")
    col1, col2 = st.columns(2)
    with col1:
        sdate= st.date_input("Start Date")
    with col2:
        edate = st.date_input("End Date")
    if st.button('Analyse'):
        col3, col4, col5 = st.columns(3)
        with col3:
            ids = ta.getids()
            selected_id = st.selectbox("", options= ids, index = 0)
            avg_price = mo.get_avg_price(selected_id, sdate, edate)
            if avg_price is not None:
                st.metric("Average Price", f"₹{avg_price:,.2f}")
            else:
                st.warning("No data found")

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