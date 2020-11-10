import csv
with open("bugetdata.csv") as budgetdata:
    readerdata = csv.reader(budgetdata) 

    for row in readerdata:
        print(row)
        
