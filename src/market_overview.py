import pymysql as ps

def get_connection():
    conn = ps.connect(
        host = "localhost",
        user = "root",
        password= "Mano_rootsql0481",
        database= "cross_market_analysis",
        cursorclass=ps.cursors.DictCursor
    )
    return conn

def get_avg_price():
    conn = get_connection()
    cursor = conn.cursor()
    queries = {"OIL":"SELECT AVG(PRICE_INR) AS AVG_PRICE FROM OIL_PRICES;",
             "BITCOIN":"SELECT AVG(PRICE_INR) AS AVG_PRICE FROM CRYPTO_PRICES WHERE COIN_ID = 'BITCOIN'",
             "S&P 500":"SELECT AVG(CLOSE) AS AVG_PRICE FROM STOCK_PRICES WHERE TICKER = 'GSPC'",
             "NIFTY":"SELECT AVG(CLOSE) AS AVG_PRICE FROM STOCK_PRICES WHERE TICKER = 'NSEI'"
             }
    results = {}
    for name, query in queries.items():
        cursor.execute(query)
        row = cursor.fetchone()
        results[name] = row["AVG_PRICE"] if row else None
    cursor.close()
    conn.close()
    return results
def get_market_comparison():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT s.DATE,
           s.CLOSE AS STOCK_PRICE,
           o.PRICE_INR AS OIL_PRICE,
           c.PRICE_INR AS BTC_PRICE
    FROM STOCK_PRICES s
    JOIN OIL_PRICES o ON s.DATE = o.DATE
    JOIN CRYPTO_PRICES c ON s.DATE = c.DATE
    WHERE s.TICKER='GSPC' AND c.COIN_ID='bitcoin'
    ORDER BY s.DATE
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows