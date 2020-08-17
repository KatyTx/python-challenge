#bring in modules
import os
import csv

#set path for files
csvpath = os.path.join('..' , 'Resources', 'budget_data.csv')

# list to store data
total_months = []
total_profitloss = []
average_change = []
greatest_increase_in_profits = []

#function that will review the budget data
def stats(budget_info):
#assigning variables in data
#assign month from column 0 and since numbers and letter made string but need to convert to integer so it can be counted
    months = (int(str(budget_info[0]))

#assign profit and loss from column 1, may need to specify in formula which are positive and which are negative
    profit_loss =int(budget_info[1])

# build out calculations of data needed
# The total number of months included in the dataset
    total_months = sum(months)

#The net total amount of "Profit/Losses" over the entire period
    total_profitloss = sum(profit_loss)

    if profit_loss >0:
        print(f'Profit is  {profit_loss})
    else:
        print(f'Losses are {profit_loss}')

#The average of the changes in "Profit/Losses" over the entire period
    average_change = mean(profit_loss)

#The greatest increase in profits (date and amount) over the entire period
    greatest_increase_in_profits = max(profit_loss)
        #need to identify month
        maxmonth = 

#The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_in_profits = min(profit_loss)
        #need to identify month
        minmonth = 


 #print out the results of the information
    print(Financial Analysis)
    print('-'*10)
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profitloss}')
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {maxmonth} {greatest_increase_in_profits}')
    print(f'Greatest Decrease in Profits: {minmonth} {greatest_decrease_in_profits')



# open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read the header 
    csv_header = next(csvreader)
    print(f"CSV Header : {csv_header}")

#loop through the data
    for row in csvreader:
        print(months)
        print(profit_loss)




