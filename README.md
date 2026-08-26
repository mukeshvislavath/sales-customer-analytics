# Sales & Customer Analytics

A Python-based project for analyzing sales, customers, products, profitability, and discount patterns using real-world sales data.

The project combines Python, Pandas, SQL, data visualization, and basic machine learning in one structured project.

## Overview

The main goal of this project was to take a raw sales dataset and turn it into useful business insights.

The analysis covers:

* Overall sales, profit, and quantity
* Sales and profit by category
* Profit at different discount levels
* Most and least profitable products
* Top customers by sales
* Yearly sales and profit
* Monthly sales trends
* Basic machine learning analysis

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* SQL
* SQLite
* Git & GitHub

## Project Structure

```text
sales-customer-analytics/
│
├── data/
│   ├── sales_data.csv
│   └── sales.db
│
├── output/
│   ├── discount_vs_profit.png
│   ├── monthly_sales_trend.png
│   ├── profit_by_category.png
│   └── sales_by_category.png
│
├── src/
│   ├── analysis.py
│   ├── ml_model.py
│   ├── sql_analysis.py
│   └── visualization.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## What I Did

The project starts by loading and checking the dataset using Pandas.

I performed basic data exploration such as:

* Checking the shape and columns
* Checking data types
* Finding missing values
* Checking duplicate records
* Generating basic statistics

I then performed different analyses using Pandas `groupby()` and aggregation functions to understand sales and profitability.

I also converted the order and shipping dates into datetime format so that I could perform yearly and monthly analysis.

For the database part, I used SQLite and SQL queries to analyze the same sales data.

Matplotlib was used to create charts for the main findings.

## Key Analysis

Some of the questions explored in the project were:

* Which categories generate the most sales?
* Which categories generate the most profit?
* How does discount affect profit?
* Which products are highly profitable?
* Which products are causing losses?
* Which customers generate the highest sales?
* How do sales and profit change over time?

## Machine Learning

The project also includes a basic machine learning component using Scikit-learn.

The purpose was to understand how machine learning can be added to a real-world data analysis project rather than keeping the project limited to exploratory analysis.

## What I Learned

This project helped me understand how different parts of Python and data analysis fit together in a real project.

I practiced:

* Working with CSV and database files
* Pandas data analysis
* Data cleaning and inspection
* Grouping and aggregation
* Date/time handling
* SQL queries with SQLite
* Data visualization with Matplotlib
* Using Scikit-learn
* Splitting code into multiple Python files
* Working with modules and imports
* Managing a virtual environment
* Using `requirements.txt`
* Using `.gitignore`
* Managing a Git repository
* Pushing a project to GitHub

One of the main things I learned was how to organize individual Python scripts into a proper project structure instead of keeping everything in one file.

## How to Run

Clone the repository:

```bash
git clone https://github.com/mukeshvislavath/sales-customer-analytics.git
```

Go to the project directory:

```bash
cd sales-customer-analytics
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python src/analysis.py
```

Run the SQL analysis:

```bash
python src/sql_analysis.py
```

Run the visualizations:

```bash
python src/visualization.py
```

Run the machine learning code:

```bash
python src/ml_model.py
```

## Future Improvements

Some improvements I would like to make in the future:

* Add an interactive dashboard
* Improve the machine learning model
* Add model evaluation and comparison
* Create an API using FastAPI
* Add automated testing
* Deploy the project

## Author

Mukesh Vislavath

GitHub: https://github.com/mukeshvislavath
