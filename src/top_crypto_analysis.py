import pymysql as ps
import querry_runner as qr
def get_connection():
    conn = ps.connect(
        host = "localhost",
        user = "root",
        password= "Mano_rootsql0481",
        database= "cross_market_analysis",
        cursorclass=ps.cursors.DictCursor
    )
    return conn

def getids():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT COIN_ID FROM CRYPTO_PRICES")
        ids = [row["COIN_ID"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return ids
    
def price_chart(ids, sdate, edate):
    query = f"""
    SELECT DATE, PRICE_INR
    FROM CRYPTO_PRICES
    WHERE COIN_ID = '{ids}'
    AND DATE BETWEEN '{sdate}' AND '{edate}'
    ORDER BY DATE
    """
    df = qr.run_query(query)
    return df

def daily_price(selected_id):
    query = f"""
    SELECT DATE, PRICE_INR
    FROM CRYPTO_PRICES WHERE COIN_ID = '{selected_id}'
    """
    df = qr.run_query(query)
    return df