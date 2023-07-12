import os 
import csv
# set path
file_path = os.path.join("..", "Resources", "election_data.csv")

# read file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip header
# initialize variables
    total_votes = 0
# create dictionary to store candidate votes
    candidate_votes = {}

# Loop through each row
    for row in csvreader:
        total_votes +=1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] =1

    candidate_list = list(candidate_votes.keys())
# caculate percentage
    candidate_percent = {}
    for candidate in candidate_list:
        votes = candidate_votes[candidate]
        percentage = format((votes / total_votes) * 100, ".2f")
        candidate_percent[candidate] = percentage

# Determine the winner based on the popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_list:
    print(f"{candidate}: {candidate_percent[candidate]}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Create a new text file for exporting the results
output_result = "election_result.txt"

# Open the file in write mode and write the results
with open(output_result, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidate_list:
        file.write(f"{candidate}: {candidate_percent[candidate]}% ({candidate_votes[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
