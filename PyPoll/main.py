import os
import csv

csvpath = os.path.join("..","..","..","RICEHOU201906DATA1","HW","03-Python","Instructions", "PyPoll", \
    "Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(f"Header:{header}")
    #counting number of voters
    total_voters = 0
    vote = 0
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
        #for c in candidates:
        #     vote_count.append(vote)
        #     if candidate == c:
        #         vote = vote + 1 #in vote_count
    #Winner: I obtained this code from thie site: https://stackoverflow.com/questions/42044090/return-the-maximum-value-from-a-dictionary
    max_value = max(vote_count.values())  # maximum value
    max_keys = [k for k, v in vote_count.items() if v == max_value] # getting all keys containing the `maximum`
    
    # print(vote_count)        
    # print(total_voters)
    # print(candidate_list)
    # print(len(candidates))
    # for c_ref in range(len(candidates)):
    #     vote_count.append(vote)
    #     vote = 0
    #     for c_raw in candidate:
    #         if c_ref == c_raw:
    #             vote_new = vote + 1
    #             vote_count = vote_new
    #             vote = vote_new
    #         # if c_ref != c_raw:
    #         #     vote = vote + 1
    #             #vote_count.append(vote)
    #vote_count.pop(0)    
    

    #     #print(candidates)
    # #print(vote_count)
    # #print(sum([len(candidates[x]) for x in candidates if isinstance(candidates[x], list)])) 
    # #print(candidates)
    #     #print(candidates_all)
    #     # for i = 1:
    #     #     for c in candidate:
    #     #         if c[i] != c[i - 1]:
    #     #             candidates2.append(str(c))
    #     # print(candidates2)
    # #print(first)
    # #print(candidates)
    # # for rows in csvreader:
    # #first = csvreader.__next__()[2]
    # # #     if str(r[2]) != " ":
    # # #         candidates_all.append(r[2])
    # # #     candidates_all.sort()
    # # #     # for c in set(candidates_all):
    # # #     #     candidates[c] = candidates_all.count(c)
    # # #     #         #candidates.append(str(c))
    # #     for i in str(rows[2]):
    # #         candidates = {i:str(rows[2]).count(i)}

    # #print(first)
    # print("OK")




    # # for r in csvreader:
    # #     for c in [candidates]:
    # #         if str(r[2]) != str(c):
    # #             candidates.append(c)
    # # print(candidates) 
    # # for rows in csvreader:
    # # #counting the months, assuming there's one data value per month
    # #     if str(rows[0]) != " ":
    # #         total_voters = total_voters + 1
    # #     if str(rows[2]) == "Khan":
    # #         c1_votes = c1_votes + 1 

    # # c1_percent = round(c1_votes / total_voters * 100, 3)
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
# # print(f'Khan:  {c1_percent}% ({c1_votes})')


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