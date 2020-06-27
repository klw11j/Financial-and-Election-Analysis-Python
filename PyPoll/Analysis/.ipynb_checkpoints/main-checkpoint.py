import os

import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    votes = [] 
    county = []
    candidates = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []
    Khan_votes = []
    Correy_votes = []
    Li_votes = []
    OTooley_votes = []
    

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

   #Count the total number of votes
    total_votes = (len(votes))

    #Count number of times candidates name appears
    for candidate in candidates:
    
        if candidate == "Khan":
            Khan.append(candidates)
            Khan_votes = len(Khan)
        elif candidate == "Correy":
            Correy.append(candidates)
            Correy_votes = len(Correy)
        elif candidate == "Li":
            Li.append(candidates)
            Li_votes = len(Li)
        else:
            OTooley.append(candidates)
            OTooley_votes = len(OTooley)

#Print summary of election results 

percentage_Khan = round(((Khan_votes / total_votes) * 100) , 2)
percentage_Correy = round(((Correy_votes / total_votes) * 100), 2)
percentage_Li = round(((Li_votes / total_votes) * 100), 2)
percentage_OTooley = round(((OTooley_votes / total_votes) * 100), 2)

#Determine the winner 

if percentage_Khan > max(percentage_Correy, percentage_Li, percentage_OTooley):
    winner = "Khan"
elif percentage_Correy > max(percentage_Khan, percentage_Li, percentage_OTooley):
    winner = "Correy"  
elif percentage_Li > max(percentage_Khan, percentage_Correy, percentage_OTooley):
    winner = "Li"
else: 
    winner = "O'Tooley"
    
#Print statements
print("Election Results") 
print("------------------------------") 
print(f"Total Votes: {total_votes}")
print("------------------------------")
print(f"Khan: {percentage_Khan}% ({Khan_votes})")
print(f"Correy: {percentage_Correy}% ({Correy_votes})") 
print(f"Li: {percentage_Li}% ({Li_votes})") 
print(f"O'Tooley: {percentage_OTooley}% ({OTooley_votes})") 
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")