import os
import csv

csvpath = os.path.join("..","..","..","RICEHOU201906DATA1","HW","03-Python","Instructions", "PyBank", \
    "Resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(f"Header:{header}")
    #counting number of months
    total_months = 0 
    total_PL = 0
    #saving the first value on the list as old value    
    change_oldmax = 0
    change_oldmin = 0
    changes = [] 
    pl = 0
    pl_list = []
    change_old = 0 

    # I could not use the first value of the list, I had to use pop(0) instead
    for rows in csvreader:
    #counting the months, assuming there's one data value per month
        if str(rows[0]) != " ":
            total_months = total_months + 1 
    #summing up the profit/losses
        if int(rows[1]) != " ":
            total_PL = total_PL + float(rows[1])
    #calculating the change
        if int(rows[1]) != 0:
            change = float(rows[1]) - change_old
            # saving the change value if it's the maximum
            if change > change_oldmax: 
                change_max_new = change
                date_max_new = str(rows[0])
                change_oldmax = round(change_max_new)
            # saving the change value if it's the minimum
            if change < change_oldmin: 
                change_min_new = change
                date_min_new = str(rows[0])
                change_oldmin = round(change_min_new)
            # creating a new list for changes to calculate average
            changes.append(change)
            
            # replacing old value by next row
            change_old = float(rows[1])

    changes.pop(0)
    length = len(changes) 
    total_changes = int(sum(changes))
    average_changes = round(total_changes / length, 2)
    max_incr = round(max(changes))
    min_decr = round(min(changes))
    total_months = round(total_months)
    total_PL = round(total_PL)

# print including formating        
print("")
print("--------------------------------------------------------------")
print("Financial Analysis")
print("--------------------------------------------------------------")
print(f'Total Months:             {total_months}')
print(f'Total Profit/Loss: ${total_PL}')
print(f'Average Change:       ${average_changes}')
print(f'Greatest Increase:  ${max_incr}    @ {date_max_new}')
print(f'Greatest Decrease: ${min_decr}    @ {date_min_new}')
print("")
print("--------------------------------------------------------------")

# creating file
print("Creating file with Financial Analysis...")

# I modified the code from https://www.guru99.com/reading-and-writing-files-in-python.html
f= open("Financial_Analysis.txt","w+")
f.write("Financial Analysis\n") 
f.write("--------------------------------------------------------------\n")
f.write(f'Total Months:             {total_months}\n')
f.write(f'Total Profit/Loss: ${total_PL}\n')
f.write(f'Average Change:       ${average_changes}\n')
f.write(f'Greatest Increase:  ${max_incr}    @ {date_max_new}\n')
f.write(f'Greatest Decrease: ${min_decr}    @ {date_min_new}\n')
f.write("\n")
f.write("--------------------------------------------------------------\n")
f.close()

# creating file
print("File created successfully")