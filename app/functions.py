#functions called upon in monthly sales
import operator

def to_USD(Number):
    Number = "${0:,.2f}".format(Number)
    return Number

def get_top_sellers(productList, myFiles):
    parallelPrices = []
    for p in productList:
        productSales = 0.0
        for item in myFiles:
            if p == item["product"]:
                productSales = productSales + item["sales_price"]
        parallelPrices.append({"product": p, "price": productSales})
    #Sorts in accending order
    parallelPrices = sorted(parallelPrices, key=operator.itemgetter("price"), reverse = True)
    return parallelPrices
