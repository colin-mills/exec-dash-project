# monthly_sales.py

# TODO: import some modules and/or packages here
import datetime
import csv


#declare variables
time = ""
dashes = "-----------------------"

# TODO: write some Python code here to produce the desired functionality...


#takes in file name as input 
#csv_file_path = input("Please enter the csv file in the data dirrectory that you would like to be read") # a relative filepath
#csv_file_path = "data/"+csv_file_path
csv_file_path = "ata/sales-201710.csv"
files = []

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
            files.append(d)
            #print(d)


    time = files[1]["date"]

    fileDate = datetime.datetime.fromisoformat(time) # strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

    print (dashes)
    print ("MONTH: " + str(fileDate.strftime("%B")) + " " + str(fileDate.year))
    print (dashes)


    #print("-----------------------")
    #print("MONTH: March 2018")
    #
    #print("-----------------------")
    #print("CRUNCHING THE DATA...")
    #
    #print("-----------------------")
    #print("TOTAL MONTHLY SALES: $12,000.71")
    #
    #print("-----------------------")
    #print("TOP SELLING PRODUCTS:")
    #print("  1) Button-Down Shirt: $6,960.35")
    #print("  2) Super Soft Hoodie: $1,875.00")
    #print("  3) etc.")
    #
    #print("-----------------------")
    #print("VISUALIZING THE DATA...")
    #

except FileNotFoundError:
    print("Please enter a correct file name")