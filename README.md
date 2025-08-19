# Visualizing-Product-Revenue-with-Python
This project connects to a small SQLite database (sales_data.db) containing a sales table with products, quantities, and prices. It calculates total quantity sold and total revenue per product using a SQL query inside Python, displays the results in a table, and visualizes revenue per product with a simple bar chart (sales_chart.png). 

# Basic Sales Summary with Python and SQLite

## Description
This project demonstrates how to use Python and SQLite to generate a basic sales summary. It connects to a small SQLite database (`sales_data.db`) containing sales records (product, quantity, and price), calculates total quantity sold and total revenue per product, and visualizes the results with a simple bar chart (`sales_chart.png`).

## Features
- Creates a SQLite database and sales table (if not already present)
- Inserts sample sales data
- Runs SQL queries inside Python to summarize sales
- Prints sales summary in tabular form
- Generates a bar chart showing revenue per product

## Files
- `sales_task.py` — Python script to run the task  
- `sales_data.db` — SQLite database containing sales data  
- `sales_chart.png` — Bar chart showing revenue per product  

## Requirements
- Python 3.x
- pandas
- ma
