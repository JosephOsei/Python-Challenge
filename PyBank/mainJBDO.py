#PyBank Challenge - JBDO

#Import modules *FIND OUT WHY CERTAIN VARIABLES ARE USED*
import os
import csv

#create a list to store the data being pulled in from the .csv file
months = []
profit_loss = []

#the define path required for the program to take to the right file
budget_csv = os.path.join('budget_data.csv')

#to open the .csv file
with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    #do not use the header 
    next(budget_reader)

    #develop a loop to go through the whole csv file
    for row in budget_reader:

        #add a date to the files
        months.append(row[0])

        #add profit/loss column
        profit_loss.append(float(row[1]))

#calculate the total number of months included in the dataset
total_months = (len(months))

#calculate the net amount of profit/losses over time
net_amount = sum(profit_loss)

#calculate average change per month
avg_change = net_amount / total_months

#calculate the greatest increase in profits
max_profit = max(profit_loss)

#utilise the index function we can find the position of the greatest INCREASE in profits to find the date
index_max = profit_loss.index(max_profit)
max_month = months[index_max]

#determine the greates decrease in loss
min_profit = min(profit_loss)

#utilise the index function we can find the position of the greatest DECREASE in profits to find the date
index_min = profit_loss.index(min_profit)
min_month = months[index_min]

#layout of the financial analysis
financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')

#print out the analysis layout
print(financial_analysis)

#Create a .txt file of analysis
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()
