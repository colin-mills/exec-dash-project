from app.functions import to_USD, get_top_sellers
import os
import csv


def test_to_USD():
    assert to_USD(4) == "$4.00" #should have two decimal points
    assert to_USD(57.9999) == "$58.00" #test rounding 
    assert to_USD(99999.99) == "$99,999.99" #test commas 
    assert to_USD(100000) == "$100,000.00" #test commas and decimals 
    assert to_USD(8.00000000001) == "$8.00" #Should round down

def test_get_top_sellers():
    #initialize a set for use and files
    productsSet = {"first", "Second"}
    productsSet.clear()
    files = []

    #populate productsSet and files
    
    with open("test/test_sales.csv", "r") as csv_file: # "r" means "open the file for reading"
        reader = csv.DictReader(csv_file) # assuming your CSV has headers
        for row in reader:
            d = {
                "date": row["date"], 
                "product": row["product"], 
                "unit_price": float(row["unit price"]), 
                "units_sold" : int(row["units sold"]), 
                "sales_price" : float(row["sales price"])
                }
            productsSet.add(d["product"])
            files.append(d)
    

    productsList = list(productsSet) #eliminates duplicates
    parallelPrices = get_top_sellers(productsList, files) #gets top sellers in accending order

    assert type(parallelPrices) == list
    assert len(parallelPrices) == 8
    assert parallelPrices[0]["product"] == "Button-Down Shirt"
    assert parallelPrices[7]["price"] == 155.40