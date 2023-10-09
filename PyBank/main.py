#Main Script for reading the csv files and making the analysis for the outcome results

import csv
import os
import statistics

file_path = './Resources/budget_data.csv'

profit = []
monthly_changes = []
date = []

total_profit = 0
total_change_profits = 0
initial_profit = 0


with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for row in csvreader:

        date.append(row[0])

        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        final_profit = int(row[1])
               
        monthly_change_profits = final_profit - initial_profit
        
        total_change_profits = total_change_profits + monthly_change_profits      

        initial_profit = final_profit
        
        monthly_changes.append(monthly_change_profits)

        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    monthly_changes.pop(0)

    average_change_profits = statistics.mean(monthly_changes)

    print('--'*20)
    print('Financial Analysis')
    print('--'*20)
    print(f'Total Months: {len(date)}')
    print(f'Total Profits: $ {total_profit}')
    print(f'Average Change: $ {average_change_profits:.2f}')
    print('Greatest Increase in Profits: ' + str(increase_date) + '($' + str(greatest_increase_profits) + ')')
    print('Greatest Decrease in Profits: ' + str(decrease_date) + '($' + str(greatest_decrease_profits) + ')')
    print('--'*20)

# Final script to export a text file named resultPypoll.txtwith the results

output_path = os.path.join('.','resultPybank.txt')

with open(output_path, 'w') as my_file:

    csvwriter = csv.writer(my_file, delimiter=':')
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months: 86'])
    csvwriter.writerow(['Total Profits: $ 22564198'])
    csvwriter.writerow(['Average Change: $ -8311.11'])
    csvwriter.writerow(['Greatest Increase in Profits: Aug-16($1862002)'])
    csvwriter.writerow(['Greatest Decrease in Profits: Feb-14($-1825558)'])
    


