# monthly_sales.py
import os
import datetime
import csv
import matplotlib.pyplot as plt
from functions import to_USD, get_top_sellers


#declare variables
time = ""
dashes = "------------------------------------"
files = []
totalSales = 0
productsSet = {"first", "Second"}
productsSet.clear()
productsList = []
parallelPrices = []

#variables that will be used in charts
product = []
sales = []
sizes = []


#takes in file name as input 
csv_file_path = input("Please enter the csv file in the data directory that you would like to be read.\nEnter in format similar format to \"sales-YYYYMM.csv:\" ") # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", csv_file_path)
 
#Citation: Used much of syntax and code samples from python notes in repository of georgetown-opim-243-201901
# link: https://github.com/prof-rossetti/georgetown-opim-243-201901
#

##########################
####open and read file####
##########################
try:
    #reads file passed by user
    with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
        reader = csv.DictReader(csv_file) # assuming your CSV has headers
        for row in reader:
            d = {
                "date": row["date"], 
                "product": row["product"], 
                "unit_price": float(row["unit price"]), 
                "units_sold" : int(row["units sold"]), 
                "sales_price" : float(row["sales price"])
                }
            totalSales = totalSales + d["sales_price"]
            productsSet.add(d["product"])
            files.append(d)


    #Parse date string to date object
    time = files[1]["date"]
    fileDate = datetime.datetime.fromisoformat(time)

    ##################
    ###Date of file###
    ##################
    print (dashes)
    print ("MONTH: " + str(fileDate.strftime("%B")) + " " + str(fileDate.year))
    print (dashes)
    print("CRUNCHING THE DATA...")
    
    ##################
    ###Output Sales###
    ##################
    print(dashes)
    print("TOTAL MONTHLY SALES   : " + to_USD(totalSales).rjust(12))
    
    #################
    ###Top Selling###
    #################
    print(dashes)
    productsList = list(productsSet) #eliminates duplicates
    parallelPrices = get_top_sellers(productsList, files) #gets top sellers in accending order

    #prints out each value in formatted order
    for prod in parallelPrices:
        print(prod["product"].ljust(22) + ": " + to_USD(prod["price"]).rjust(12))

        #also append lists for bar chart
        product.append(prod["product"])
        sales.append(prod["price"])
        sizes.append(prod["price"]/totalSales)

    ###################
    #####Bar Graph#####
    ###################
    input("When ready for bar graph press ENTER...\n(Please adjust window setting on graph for proper display)")

    #initialize graph aspects
    plt.bar(product, sales)
    plt.rcParams.update({'font.size': 10})
    plt.title("Bar Chart of Product Sales")
    plt.ylabel("Sales in USD ($)")
    plt.xlabel("Products")
    plt.show()

    ###################
    #####Pie Chart#####
    ###################
    input("When ready for pie chart press ENTER...\n(Please adjust window setting on graph for proper display)")
   
    #initialize pie chart aspects
    fig1, ax1 = plt.subplots()
    plt.rcParams.update({'font.size': 10})
    ax1.set_title("Pie Chart of Product Sales", loc="left")
    ax1.pie(sizes, labels=product, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis("equal")
    plt.show()

    #Citation: Used Matplotlib documentation for syntax as to how to use package
    # link: https://matplotlib.org
    #

except FileNotFoundError:
    print("\nCould not find selected file,\n Please ensure you have the correct name and try again...\n\n")