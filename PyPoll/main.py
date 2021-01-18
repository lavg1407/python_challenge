#Due to the fact I couldn't use os and the function os.path.join 
    #I use Pathlib
from pathlib import Path
import csv

election_data = Path("C:/Users/lavg1/python_challenge/PyPoll/Resources/election_data.csv")

#define variables
total_votes = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# Open and read csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #grab first row
    firstrow = next(csvreader)

#total votes
#complete list of candidates who received votes
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# % of votes each candidate won
for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes)*100,2)

# winner of election based on popular vote
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

output_path = Path('C:/Users/lavg1/python_challenge/PyPoll/Analysis/Election_Results.txt')

with open(output_path, 'w') as file:
    file.write(f"Election Results\n")
    file.write(f"-------------------------------------\n")
    file.write(f"Total Votes:" + str(total_votes) + "\n")
    file.write(f"-------------------------------------\n")
    for key, value in candidates.items():
        file.write( key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")\n")
    file.write(f"-------------------------------------\n")
    file.write(f"Winner: " + winner + "\n")
    file.write(f"-------------------------------------\n")