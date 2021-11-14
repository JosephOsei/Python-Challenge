#PyPoll Challenge - JBDO

#Import modules os and csv
import os
import csv

#the defined path required for the program to take to the right file
voter_csv = os.path.join('election_data.csv')

#create an empty dictionary to store vote count from the .csv file
vote_count = {}

#create an empty dictionary to store vote percentage
vote_per = {}

#a variable to hold the total vote count summarised
vote_total = 0

#to open the .csv file
with open(voter_csv, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

    #dont use the header from .csv file
    next(voterreader)

    #loop to iterrate through the all the rows of data
    for row in voterreader:

        #count of total votes
        vote_total += 1

        #count of votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         #condition for if the candidate does not exist in the dictionary created, to add candidate and set to value 1
        else:
            vote_count[row[2]] = 1

#variable to hold the count of the winner votes
winner_count = 0

#loop to iterrate through dictionary in order to calculate the vote percentage and to determine the winner
for candidate in vote_count:
    
    #formula to calculate vote percentage
    vote_per[candidate] = (vote_count[candidate] / vote_total) * 100

    #decide on the winnner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#Print  results and write them to a text file
results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------\n''')

    print(f'''\nElection Results
-------------------------
Total Votes: {vote_total}
-------------------------''')

    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_per[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {vote_per[candidate]:.3f}% ({votes})''')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')

    print(f'''-------------------------
Winner: {winner}
-------------------------''')

