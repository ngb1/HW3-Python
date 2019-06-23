import os
import csv

csvpath = os.path.join("budget_data.csv")

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
            # date_ch = float(rows[0]) 
            # changes.append(date_ch)
            changes.append(change)
            change_old = float(rows[1])
            # A = enumerate(rows)
            # for c in changes:
            #     c = float(rows[1])*1
            #     changes.append(enumerate(int(c)))
        #length = len((rows[1]))
        # total changes
        total_changes = int(sum(changes))
        length = int(len(changes))
    max_incr = round(max(changes))
    min_decr = round(min(changes))
    total_months = round(total_months)
    total_PL = round(total_PL)
    average_changes = round(total_changes / length, 2)



        
print("")
print("--------------------------------------------------------------")
print("Financial Analysis")
print("--------------------------------------------------------------")
print(f'Total Months:            {total_months}')
print(f'Total Profit/Loss: {total_PL}')
print(f'Average Change:       {average_changes}')
print(f'Greatest Increase:  {max_incr}    @ DD/MM')
print(f'Greatest Decrease: {min_decr}    @ DD/MM')
print("")
print("--------------------------------------------------------------")
