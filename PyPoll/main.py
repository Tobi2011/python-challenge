import os
import csv

election_data = os.path.join('election_data.csv')
election_results = os.path.join('election_results.txt')
with open(election_data, newline='') as ed:
    edata = csv.reader(ed, delimiter = ',')
    header = next(edata)
    
    total_vote_count = 0
    candidates = []
    vote_count = []
    votepercent = []
    winner = ''
    for row in edata:
        total_vote_count += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_count.append(1)
        elif row[2] in candidates:
            for i in range(len(candidates)):
                if row[2] == candidates[i]:
                    vote_count[i] += 1
                    if vote_count[i] == max(vote_count):
                        winner = candidates[i]
    for p in range(len(vote_count)):
        votepercent.append(format(vote_count[p]/total_vote_count*100,'.3f'))
    
    print ('Election Results')
    print ('-------------------------------')
    print (f'Total Vote_count: {total_vote_count}')
    print ('-------------------------------')
    for i in range(len(candidates)):
        print (f'{candidates[i]}: {votepercent[i]}% ({vote_count[i]})')

    print ('-------------------------------')
    print (f'Winner: {winner}')
    print ('-------------------------------')

with open(election_results, 'w', newline='') as br:

    br.write ('Election Results \n')
    br.write ('-------------------------------\n')
    br.write (f'Total Vote_count: {total_vote_count}\n')
    br.write ('-------------------------------\n')
    for i in range(len(candidates)):
        br.write (f'{candidates[i]}: {votepercent[i]}% ({vote_count[i]})\n')

    br.write ('-------------------------------\n')
    br.write (f'Winner: {winner}\n')
    br.write ('-------------------------------')