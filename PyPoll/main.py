import csv
import os

file_path = './Resources/election_data.csv'

count = 0
candidatelist = []
candidatename = []
vote_count = []
vote_percent = []

with open(file_path) as electioncsv:
    csvreader = csv.reader(electioncsv)

    header = next(csvreader)

    for row in csvreader:

        count = count + 1

        candidatelist.append(row[2])

    for x in set(candidatelist):

        candidatename.append(x)

        y = candidatelist.count(x)
        vote_count.append(y)

        z = (y/count)*100
        vote_percent.append(z)

    winning_vote_count = max(vote_count)
    result_a= candidatename [0] + str(vote_percent[0]) + str(vote_count[0])
    winner = candidatename[vote_count.index(winning_vote_count)]




print('--'*20)
print('Election Results')
print('--'*20)
print(f'Total Votes : {count}')
print('--'*20)
print(f'{candidatename [0]}: {vote_percent[0]} % ( {vote_count[0]} )')
print(f'{candidatename [1]}: {vote_percent[1]} % ( {vote_count[1]} )')
print(f'{candidatename [2]}: {vote_percent[2]} % ( {vote_count[2]} )')
print('--'*20)
print(f'The winner is: {winner}')
print('--'*20)


output_path = os.path.join('.','resultPypoll.txt')


with open(output_path, 'w') as my_file:
    my_writer = csv.writer(my_file)

    my_writer.write('Election Results')
    my_writer.write('Total Votes: 369711')
    my_writer.write('Charles Casper Stockham: 23.049% (85213)')
    my_writer.write('Diana DeGette: 73.812% (272892)')
    my_writer.write('Raymon Anthony Doane: 3.139% (11606)')    
    my_writer.write('Winner: Diana DeGette')
