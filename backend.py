import psycopg2
import pandas as pd

# Database connection
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="finance",
        user="postgres",
        password="Yash"
    )

# CREATE
def add_transaction(transaction_id, transaction_date, description, amount, type_):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO transactions (transaction_id, transaction_date, description, amount, type)
        VALUES (%s, %s, %s, %s, %s)
    """, (transaction_id, transaction_date, description, amount, type_))
    conn.commit()
    cur.close()
    conn.close()

# READ
def get_transactions(filter_type=None, sort_by=None, ascending=True):
    conn = get_connection()
    query = "SELECT * FROM transactions"
    if filter_type:
        query += f" WHERE type = '{filter_type}'"
    if sort_by:
        query += f" ORDER BY {sort_by} {'ASC' if ascending else 'DESC'}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# UPDATE
def update_transaction(transaction_id, transaction_date, description, amount, type_):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE transactions
        SET transaction_date = %s, description = %s, amount = %s, type = %s
        WHERE transaction_id = %s
    """, (transaction_date, description, amount, type_, transaction_id))
    conn.commit()
    cur.close()
    conn.close()

# DELETE
def delete_transaction(transaction_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE transaction_id = %s", (transaction_id,))
    conn.commit()
    cur.close()
    conn.close()

# Aggregations
def get_aggregates():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            COUNT(*) AS total_transactions,
            SUM(CASE WHEN type = 'Revenue' THEN amount ELSE 0 END) AS total_revenue,
            SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END) AS total_expense,
            AVG(amount) AS avg_amount,
            MIN(amount) AS min_amount,
            MAX(amount) AS max_amount
        FROM transactions
    """)
    result = cur.fetchone()
    conn.close()
    return result