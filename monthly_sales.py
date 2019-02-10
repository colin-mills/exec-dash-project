# monthly_sales.py

# TODO: import some modules and/or packages here
import datetime
import csv


#declare variables
time = ""
dashes = "------------------------------------"
files = []
totalSales = 0
productsSet = {"first", "Second"}
productsSet.clear()
productsList = []
parallelPrices = []
productSales = 0.0

# TODO: write some Python code here to produce the desired functionality...


#takes in file name as input 
#csv_file_path = input("Please enter the csv file in the data dirrectory that you would like to be read") # a relative filepath
#csv_file_path = "data/"+csv_file_path
csv_file_path = "data/sales-201803.csv"

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
    fileDate = datetime.datetime.fromisoformat(time) # strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

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
    totalSales_USD = "${0:,.2f}".format(totalSales)
    print(dashes)
    print("TOTAL MONTHLY SALES: " + totalSales_USD)
    
    
    
    #################
    ###Top Selling###
    #################
    print(dashes)
    productsList = list(productsSet)
    for p in productsList:
        productSales = 0
        for item in files:
            if p == item["product"]:
                productSales = productSales + item["sales_price"]
        parallelPrices.append({"product": p, "price": productSales})

    print(parallelPrices)

    #(item["units_sold"] * 
    #print("TOP SELLING PRODUCTS:")
    #print("  1) Button-Down Shirt: $6,960.35")
    #print("  2) Super Soft Hoodie: $1,875.00")
    #print("  3) etc.")
    #
    #print("-----------------------")
    #print("VISUALIZING THE DATA...")
    #




























except FileNotFoundError:
    print("\nCould not find selected file,\n Please ensure you have the correct name and try again...\n\n")