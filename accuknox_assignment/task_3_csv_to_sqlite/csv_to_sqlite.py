#Task 3
import pandas as pd
import sqlite3

#import the csv file
df = pd.read_csv("Mall_Customers.csv")

conn = sqlite3.connect("customer.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer(
  CustomerID INTEGER PRIMARY KEY ,
  Gender TEXT,
  Age INTEGER,
  Annual_income INTEGER,
  Spending_score INTEGER
)
""")
# save the data from the csv file to the database
df.to_sql("customer",conn,if_exists="replace",index=False)

conn.commit()

# print the data in the database
query_data = pd.read_sql_query("select * from customer",conn)
print("\nData in the database:-\n")
print(query_data)

conn.close()
