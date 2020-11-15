import os
import csv

total_votes = 0
candidates = []
PerCandidates = []

csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    for row in csvreader:
        total_votes += 1
        if total_votes == 1:
            candidates.append(row[2])
            PerCandidates.append(1)
        else:
            try:
                icandidate = candidates.index(row[2])
                PerCandidates[icandidate] += 1
            except:
                candidates.append(row[2])
                PerCandidates.append(1)

results = []
results.append("Election Results\n")
results.append(f"Total Votes: {total_votes}\n")

winner = candidates[0]
maxvotes = PerCandidates[0]
for i in range(len(candidates)):
    if PerCandidates[i] > maxvotes:
        winner = candidates[i]
        maxvotes = PerCandidates[i]
    percent = 100 * PerCandidates[i] / total_votes
    results.append(f"{candidates[i]}: {round(percent,3)} % ({PerCandidates[i]})")

results.append(f"\nWinner: {winner}\n")

filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
