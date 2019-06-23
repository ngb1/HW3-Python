import os
import csv

csvpath = os.path.join("..","..","..","RICEHOU201906DATA1","HW","03-Python","Instructions", "PyPoll", "Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(f"Header:{header}")