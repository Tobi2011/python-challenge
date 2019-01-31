import os
import csv

budget_data = os.path.join('budget_data.csv')
budget_results = os.path.join('budget_results.txt')
with open(budget_data, newline='') as bd:
    bdata = csv.reader(bd, delimiter = ',')
    header = next(bdata)
    
    total_months = 0
    net_money = 0
    avg_change = 0
    porl = []
    porldate = []
    change = 0
    tchange = 0
    great_increase = 0
    date_increase = ''
    great_decrease = 0
    date_decrease = ''

    for row in bdata:
        total_months += 1
        net_money += int(row[1])
        porl.append(int(row[1]))
        porldate.append(row[0])

    for i in range(len(porl)-1):
        change = porl[i+1] - porl[i]
        tchange += change
        if change > great_increase:  
            great_increase = change
            date_increase = porldate[i+1]
        elif change < great_decrease:
            great_decrease = change
            date_decrease = porldate[i+1]

    avg_change = format(tchange/(total_months-1),'.2f')

    print ('Financial Analysis')
    print ('-------------------------------')
    print (f'Total Months: {total_months}')
    print (f'Total: ${net_money}')
    print (f'Average Change: {avg_change}')
    print (f'Greatest Increase in Profits: {date_increase} (${great_increase})')
    print (f'Greatest Decrease in Profits: {date_decrease} (${great_decrease})')

with open(budget_results, 'w', newline='') as br:

    br.write('Financial Analysis \n')
    br.write('-------------------------------')

    br.write(f'Total Months: {total_months}\n')
    br.write(f'Total: ${net_money}\n')
    br.write(f'Average Change: {avg_change}\n')
    br.write(f'Greatest Increase in Profits: {date_increase} (${great_increase})\n')
    br.write(f'Greatest Decrease in Profits: {date_decrease} (${great_decrease})')