import os
import csv

csvpath = os.path.join("..","..","..","RICEHOU201906DATA1","HW","03-Python","Instructions", "PyBank", "Resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(f"Header:{header}")
    #counting number of months
    total_months = 0 
    total_PL = 0  
    change_old = 867884
    changes = [] 
    for rows in csvreader:
        if str(rows[0]) != " ":
            total_months = total_months + 1 
    #summing up the profit/losses
        if str(rows[1]) != " ":
            total_PL = total_PL + float(rows[1])
        if str(rows[1]) != " " and float(rows[1]) != change_old:
            change = float(rows[1]) - change_old
            changes.append(change)
            change_old = change
            # A = enumerate(rows)
            # for c in changes:
            #     c = float(rows[1])*1
            #     changes.append(enumerate(int(c)))
        #length = len((rows[1]))
        # total changes
        total_changes = int(sum(changes))
        length = int(len(changes))
        average_changes = total_changes) / length
        

print("Financial Analysis")
print("------------------------------")
print(f'Total Months:      {total_months}')
print(f'Total Profit/Loss: {total_PL}')
print(f'Average Change:    {average_changes}')
print(length)
print(total_changes)
#print(average_changes)