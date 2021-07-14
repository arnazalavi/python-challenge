# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
Total_Votes = 0
candidates_list =[]
#candidates_votes = [0]*len(candidates_list)
#candidates_votes = [0]*4
candidates_votes = []
candidates_list_index = 0
candidates_votes_percent = 0

#Create a candidate list and Candidate vote list
def candidates_list_check(candidate_name):
            # if candidates not in candidates list then add to a list
            if (candidate_name not in candidates_list):
                
                candidates_list.append(candidate_name)
                candidates_index = candidates_list.index(candidate_name)
                candidates_votes.append(0)

# function return the winner of the election
def election_winner():
    return candidates_list[candidates_votes.index(max(candidates_votes))]

#csvpath = os.path.join("..","Resources","election_data.csv")
csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath,"r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
# Go through each row in the file 
#get the index from the candidates list using name as index
# Add the candidates votes to a candidates votes list 
    for row  in csvreader:
        candidates_list_check(row[2])
        candidates_list_index = candidates_list.index(row[2])
        candidates_votes[candidates_list_index] = candidates_votes[candidates_list_index] +1 
    
    Total_Votes = sum(candidates_votes)

    print(f"Election Result")
    print(f"-----------------")
    print(f" Total Votes:{Total_Votes}")
    print(f"-----------------")
    
    for i in  range(len(candidates_list)):
        # get the index of a candidate from candidate list
        # use the index to go to candidates_votes list and get the votes
        #print(candidates_list[i])
        candidates_list_index = candidates_list.index(candidates_list[i])
        candidates_votes_percent = round(((candidates_votes[candidates_list_index] / Total_Votes) * 100),2)
        #candidates_votes_percent = candidates_votes[candidates_list_index] / Total_Votes * 100
        print(f"{candidates_list[i]}: {candidates_votes_percent}%  ({candidates_votes[candidates_list_index]})")
 
Election_Winner =election_winner() 
print(f"-----------------")
print(f"Election Winner : {Election_Winner}")
print(f"-----------------")

# Open the file using "write" mode. Specify the variable to hold the contents
with open("analysis/Election_Result.txt", 'w', newline='') as output:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
    print(f"Election Result", file = output)
    print(f"-----------------", file = output)
    print(f" Total Votes:{Total_Votes}", file = output)
    print(f"-----------------", file = output)
    for i in  range(len(candidates_list)):
        # get the index of a candidate from candidate list
        # use the index to go to candidates_votes list and get the votes
        #print(candidates_list[i])
        candidates_list_index = candidates_list.index(candidates_list[i])
        candidates_votes_percent = round(((candidates_votes[candidates_list_index] / Total_Votes) * 100),2)
        #print(candidates_votes_percent)
        #candidates_votes_percent = candidates_votes[candidates_list_index] / Total_Votes * 100
        print(f"{candidates_list[i]}: {candidates_votes_percent}%  ({candidates_votes[candidates_list_index]})", file=output)
    print(f"-----------------", file = output)
    print(f"Election Winner : {Election_Winner}",file = output)
    print(f"-----------------", file = output)