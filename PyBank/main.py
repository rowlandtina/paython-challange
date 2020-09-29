#import budget data 
import os
import csv 


#working directory

csvpath=os.path.join('Resources','budget_data.csv')

analysis_file = os.path.join("analysis","tina_analysis_output.txt")
analysis_output = open(analysis_file,'w')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    
    # increase = []
    # decrease = []
    monthly = []
    revenue_change = []
    revenue_profit_change = []
    monthly_profit_change = []
    
    #print(f"Header: {csv_header}")               

#Monthly       
    for row in csvreader:
        monthly.append(row[0])
        revenue_change.append(row[1])
    #print(len(monthly))

 #Rev change 
    revenue_int = map(int,revenue_change)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

 #Avg Change
    x = 0
    for x in range(len(revenue_change) - 1):
        profit_loss = int(revenue_change[x+1]) - int(revenue_change[x])

 # append profit_loss
        revenue_profit_change.append(profit_loss)
    Total = sum(revenue_profit_change)

    #print(revenue_profit_change)
    monthly_profit_change = Total / len(revenue_profit_change)
    #print(monthly_profit_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_profit_change)
    #print(profit_increase)
    p = revenue_profit_change.index(profit_increase)
    monthly_increase = monthly[p+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_profit_change)
    #print(profit_decrease)
    d = revenue_profit_change.index(profit_decrease)
    monthly_decrease = monthly[d+1]


Avg_total = round(float(monthly_profit_change),2)

#Print Statements

print(f'Financial Analysis')
analysis_output.write('Financial Analysis')
print(f'----------------------------'+'\n')
analysis_output.write('----------------------------'+'\n')

print("Total number of months: " + str(len(monthly)))
analysis_output.write('Total number of months: ' + str(len(monthly)))
print("Total Revenue in period: $ " + str(total_revenue))
analysis_output.write('Total Revenue in period: $' + str(total_revenue))    
print("Average monthly change in Revenue : $" + str(Avg_total))
analysis_output.write('Average monthly change in Revenue : $' + str(Avg_total))
print(f"Greatest Increase in Profits: {monthly_increase} (${profit_increase})")
analysis_output.write(f'Greatest Increase in Profits: {monthly_increase} (${profit_increase})')
print(f"Greatest Decrease in Profits: {monthly_decrease} (${profit_decrease})")
analysis_output.write(f'Greatest Decrease in Profits: {monthly_decrease} (${profit_decrease})')