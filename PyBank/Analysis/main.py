#bring in modules
import os
import csv

#set path for files
csvpath = os.path.join('..' , 'Resources', 'budget_data.csv')

# open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read the header 
    csv_header = next(csvreader)
    #print(f"CSV Header : {csv_header}")

    #tried to skip header but distorts numbers
    #next(csvreader)

# list to store data
    months_list = []
    profitloss_list = []
    month_change =[]
    prior_amt = 0
    month_count = []
    sum_avg_change =[]
    first_monthrow = True

#loop through the data
    for row in csvreader:
      
#assigning variables in data
#assign month from column 0 and since numbers and letter made string but need to convert to integer so it can be counted
          months = str(row[0])
          months_list.append(months)

            
#assign profit and loss from column 1
          profit_loss = int(row[1])
          profitloss_list.append(profit_loss)
                           
          change = int(row[1]) - prior_amt
          prior_amt = int(row[1])
          #print(change)
          month_change.append(change)
          month_count.append(0)

          if first_monthrow == False:
            sum_avg_change.append(change)
          first_monthrow = False
     

          i = month_change.index(change)
          month_count[i]+=1
          #print(i)

#outside loop count of all months        
total_months = len(month_change)
#print(total_months)

#outside loop that totals all profit and loss
total_profit_loss = sum(profitloss_list)
#print(total_profit_loss)

#outside loop calculation of average of the changes
#avg_change = sum(month_change)/total_months

avg_change = round(sum(sum_avg_change)/len(sum_avg_change),2)
#print(avg_change)

# change_list = []
#loop through the month change data to extract info
for i in month_change:

#extracted index related to highest change month change and then combined information needed for output
  increase_index = month_change.index(max(month_change))
#print (increase_index)
increase = months_list[increase_index] + " ($" + str(month_change[increase_index]) + ")"
#print(increase)

#extracted index related to lowest change month change and then combined information needed for output
decrease_index = month_change.index(min(month_change))
#print(decrease_index)
decrease = months_list[decrease_index] + " ($" + str(month_change[decrease_index]) + ")"
#print(decrease)

#detail that results will go in text file 
results_output = "bankoutput.txt"
#print(results_output)

#write output data in new txt file
results_file = open(results_output, 'w') 

output_string = "Financial Analysis"
print(output_string)
results_file.write(output_string+"\n") 

output_string = ('-'*10)
print(output_string)
results_file.write(output_string+"\n") 

output_string = (f'Total Months: {total_months}')
print(output_string)
results_file.write(output_string+"\n") 

output_string = (f'Total: $ {total_profit_loss}')
print(output_string)
results_file.write(output_string+"\n") 

output_string = (f'Average Change: $ {avg_change}')
print(output_string)
results_file.write(output_string+"\n") 

output_string = (f'Greatest Increase in Profits: {increase}')
print(output_string)
results_file.write(output_string+"\n") 

output_string = (f'Greatest Decrease in Profits: {decrease}')
print(output_string)
results_file.write(output_string+"\n") 

# #flushes information from ram since writing to txt file
results_file.flush()
#closes the file after
results_file.close()
