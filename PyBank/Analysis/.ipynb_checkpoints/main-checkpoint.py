import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

total_months = []
total_profit = []
profit_change = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #find monthly change in profit by iterating through the profits
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-(total_profit[i]))

    #find greatest increase and decrease in profits
    greatest_increase_profits = max(profit_change)
    greatest_decrease_profits = min(profit_change)
    
    #greatest increase month
    k = profit_change.index(greatest_increase_profits)
    greatest_increase_month = total_months[k+1]

    #greatest decrease month
    j = profit_change.index(greatest_decrease_profits)
    greatest_decrease_month = total_months[j+1]

#print statements
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits:{greatest_increase_month} (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits:{greatest_decrease_month} (${greatest_decrease_profits})")        

        
