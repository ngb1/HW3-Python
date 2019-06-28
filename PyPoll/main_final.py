import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(f"Header:{header}")
    #counting number of voters
    total_voters = 0
    candidate_list = []
    vote_count = {}
    percent_count = {}
    vote_list = []
    for rows in csvreader:
        voter = rows[0]
        county = rows[1]
        candidate = rows[2]
        #counting number of voters
        if voter != " ":
            total_voters = total_voters + 1
        #option 1: updating the voter count per candidate using candidate as index in the vote_count dictionary
        if candidate in vote_count:
            vote_count[candidate] = vote_count[candidate] + 1
            percent_count[candidate] = round(vote_count[candidate] * 100 / total_voters,3)
        else:
            vote_count[candidate] = 1
        #option 2: creating a list from the candidates list
        if candidate not in candidate_list:
            #updating the candidates list
            candidate_list.append(candidate) 
            vote_list.append(1)
        
    #Winner: I obtained this code from thie site: https://stackoverflow.com/questions/42044090/return-the-maximum-value-from-a-dictionary
    max_value = max(vote_count.values())  # maximum value
    max_keys = [k for k, v in vote_count.items() if v == max_value] # getting all keys containing the `maximum`
   #printing results
print("")
print("Election Results")
print("--------------------------------------------------------------------------------------------------------")
print(f'Total votes:  {total_voters}')
print("--------------------------------------------------------------------------------------------------------")
print(f'Candidates:  {candidate_list}')
print(f'Votes:       {vote_count}')
print(f'Percent (%): {percent_count}')
print("")
print("--------------------------------------------------------------------------------------------------------")
print(f'Winner:      {max_keys}')
print("")
print("--------------------------------------------------------------------------------------------------------")

# creating file
print("Creating file with Election Results...")

# I modified the code from https://www.guru99.com/reading-and-writing-files-in-python.html
f= open("Election_Results.txt","w+")
f.write("Election Results\n") 
f.write("----------------------------------------------------------------------------------------------------------------------------\n")
f.write(f'Total votes:  {total_voters}\n')
f.write(f'Candidates:  {candidate_list}\n')
f.write(f'Votes:       {vote_count}\n')
f.write(f'Percent (%): {percent_count}\n')
f.write("\n")
f.write(f'Winner:      {max_keys}\n')
f.write("----------------------------------------------------------------------------------------------------------------------------\n")
f.close()

# creating file
print("File created successfully")