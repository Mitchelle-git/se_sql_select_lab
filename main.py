# STEP 1A
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("database.db")


# STEP 2
# First five rows
df_first_five = pd.read_sql_query("SELECT * FROM sales LIMIT 5", conn)

# STEP 3
# Five rows in reverse order
df_five_reverse = pd.read_sql_query("SELECT * FROM sales ORDER BY id DESC LIMIT 5", conn)

# STEP 4
# Alias column
df_alias = pd.read_sql_query("SELECT name AS alias FROM sales", conn)

# STEP 5
# Executive records
df_executive = pd.read_sql_query("SELECT * FROM sales WHERE title = 'Executive'", conn)

# STEP 6
# Name length
df_name_length = pd.read_sql_query(
    "SELECT name, LENGTH(name) AS name_length FROM sales",
    conn
)

# STEP 7
# Short titles (adjust number if needed by tests)
df_short_title = pd.read_sql_query(
    "SELECT * FROM sales WHERE LENGTH(title) < 10",
    conn
)

# STEP 8
# Total price sum
sum_total_price = pd.read_sql_query(
    "SELECT SUM(price) AS total_price FROM sales",
    conn
)

# STEP 9
# Day, month, year from date column
df_day_month_year = pd.read_sql_query(
    """
    SELECT 
        date,
        strftime('%d', date) AS day,
        strftime('%m', date) AS month,
        strftime('%Y', date) AS year
    FROM sales
    """,
    conn
)
