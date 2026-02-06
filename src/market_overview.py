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

def getids():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT ID, MARKET_CAP_RANK FROM CRYPTOCURRENCIES ORDER BY MARKET_CAP_RANK")
        ids = [row["ID"] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return ids

def get_price(selected_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT CURRENT_PRICE FROM CRYPTOCURRENCIES WHERE ID = %s"
    cursor.execute(query, (selected_id))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row["CURRENT_PRICE"] if row else None

def get_avg_price(selected_id, sdate, edate):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT AVG(PRICE_INR) AS AVERAGE_PRICE FROM CRYPTO_PRICES WHERE COIN_ID = %s AND DATE >= '{sdate}' AND DATE <= '{edate}'"
    cursor.execute(query, (selected_id))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row["AVERAGE_PRICE"] if row else None