import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS sales (product TEXT, quantity INTEGER, price REAL)""")
sample_data = [('Laptop', 5, 800), ('Phone', 10, 500), ('Tablet', 7, 300)]
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

query = """SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"""
df = pd.read_sql_query(query, conn)
conn.close()

print("Sales Summary:")
print(df)

df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.ylabel('Revenue ($)')
plt.title('Revenue per Product')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
