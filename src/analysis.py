import pandas as pd

# Load the dataset
df = pd.read_csv("data/sales_data.csv")

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset shape
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Total profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Total quantity sold
total_quantity = df["Quantity"].sum()
print("Total Quantity Sold:", total_quantity)

# Average order value
average_sales = df["Sales"].mean()
print("Average Sales per Transaction:", average_sales)


# Sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Sales and profit by category
category_performance = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\nCategory Performance:")
print(category_performance)


# Profit by discount level
discount_profit = df.groupby("Discount")["Profit"].agg(["sum", "mean", "count"])

print("\nProfit by Discount:")
print(discount_profit)


# Profit by product
product_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Most Profitable Products:")
print(product_profit.head(10))

print("\nTop 10 Least Profitable Products:")
print(product_profit.tail(10))

# Extract year from order date
df["Year"] = df["Order Date"].dt.year

# Yearly sales and profit
yearly_performance = df.groupby("Year")[["Sales", "Profit"]].sum()

print("\nYearly Performance:")
print(yearly_performance)

# Customer performance
customer_performance = (
    df.groupby("Customer Name")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("\nTop 10 Customers by Sales:")
print(customer_performance.head(10))

