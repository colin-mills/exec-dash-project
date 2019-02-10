# monthly_sales.py

import datetime
import csv


# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

csv_file_path = "data/sales-201710.csv" # a relative filepath
files = []

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        d = {"date": row["date"], "product": row["product"], "unit_price": float(row["unit price"]), "units_sold" : int(row["units sold"]), "sales_price" : float(row["sales price"])}
        #print(type(d), d["name"], d["price"])
        files.append(d)

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
