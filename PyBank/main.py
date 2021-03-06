#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

import os
import csv

#path

csvpath = os.path.join('budget_data.csv')

#variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest = 0
greatest_month = 0
greatest_dec = 0
greatest_month = 0

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
#revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest = int(row[1])
    greatest_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        #change in month
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #greatest increase
        if int(row[1]) > greatest:
            greatest = int(row[1])
            greatest_month = row[0]
            
        #greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_month = row[0]  
      
    #average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print("Change:"+ str(average_change))
    print(greatest_month, max(changes))
    print(greatest_dec_month, min(changes))

    PyBank = open("output.txt","w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(total_months)) 
    PyBank.write('\n' +"Total Amount" + str(total_revenue)) 
    PyBank.write('\n' +"Average" + str(average_change)) 
    PyBank.write('\n' +greatest_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_dec_month) 
    PyBank.write('\n' +str(low))     
        