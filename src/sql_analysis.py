import sqlite3
import pandas as pd


# -----------------------------
# 1. Load data
# -----------------------------

df = pd.read_csv("data/sales_data.csv")


# -----------------------------
# 2. Create SQLite database
# -----------------------------

connection = sqlite3.connect("data/sales.db")

df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

print("Sales data loaded into SQLite database.")


# -----------------------------
# 3. SQL Query: Sales by Category
# -----------------------------

query = """
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSales by Category:")
print(result)


# -----------------------------
# 4. SQL Query: Profit by Category
# -----------------------------

query = """
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nProfit by Category:")
print(result)


# -----------------------------
# 5. SQL Query: Sales by Region
# -----------------------------

query = """
SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSales by Region:")
print(result)


# -----------------------------
# 6. SQL Query: Top 10 Customers
# -----------------------------

query = """
SELECT
    "Customer Name",
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Customer Name"
ORDER BY Total_Sales DESC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\nTop 10 Customers by Sales:")
print(result)


# -----------------------------
# 7. SQL Query: Loss-Making Products
# -----------------------------

query = """
SELECT
    "Product Name",
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY "Product Name"
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC
LIMIT 10;
"""

result = pd.read_sql_query(query, connection)

print("\nTop 10 Loss-Making Products:")
print(result)


# -----------------------------
# 8. SQL Query: Discount vs Profit
# -----------------------------

query = """
SELECT
    Discount,
    SUM(Profit) AS Total_Profit,
    AVG(Profit) AS Average_Profit,
    COUNT(*) AS Transactions
FROM sales
GROUP BY Discount
ORDER BY Discount;
"""

result = pd.read_sql_query(query, connection)

print("\nProfit by Discount:")
print(result)


# -----------------------------
# 9. Close database connection

connection.close()

print("\nDatabase connection closed.")